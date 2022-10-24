import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity



movies = pd.read_csv('data/movies.csv')
tags = pd.read_csv('data/tags.csv')
ratings = pd.read_csv('data/ratings.csv')

movies['genres'] = movies['genres'].str.replace('|',' ')

movies = movies[movies.movieId.isin(ratings.movieId.unique().tolist())]

merged = pd.merge(movies, tags, on='movieId', how='left')
merged.fillna("", inplace=True)
merged = pd.DataFrame(merged.groupby('movieId')['tag'].apply(lambda x: "%s" % ' '.join(x)))
merged_df = pd.merge(movies, merged, on='movieId', how='left')
merged_df['metadata'] = merged_df[['tag', 'genres']].apply(lambda x: ' '.join(x), axis = 1)


#Content Latent Matrix from metadata
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(merged_df['metadata'])
count_df = pd.DataFrame(count_matrix.toarray(), index=merged_df.index.tolist())


# Apply SVD
svd = TruncatedSVD(n_components=25)
latent_df = svd.fit_transform(count_df)
n = 25
latent_df = pd.DataFrame(latent_df[:,0:n], index=merged_df.title.tolist())
latent_df.shape


# Collaborative Latent Matrix from user ratings
# Merge
ratings1 = pd.merge(movies[['movieId']], ratings, on="movieId", how="right")
# Pivot
ratings2 = ratings1.pivot(index = 'movieId', columns ='userId', values = 'rating').fillna(0)

svd = TruncatedSVD(n_components=200)
latent_df_2 = svd.fit_transform(ratings2)
latent_df_2 = pd.DataFrame(latent_df_2, index=merged_df.title.tolist())


def recommend(option_1,option_2):

    # Get the latent vectors for "Toy Story" from content and collaborative matrices
    v1 = np.array(latent_df.loc[option_1]).reshape(1, -1)
    v2 = np.array(latent_df_2.loc[option_1]).reshape(1, -1)

    v3 = np.array(latent_df.loc[option_2]).reshape(1, -1)
    v4 = np.array(latent_df_2.loc[option_2]).reshape(1, -1)

    # Compute the cosine similartity of this movie with the others in the list
    sim1 = cosine_similarity(latent_df, v1).reshape(-1)
    sim2 = cosine_similarity(latent_df_2, v2).reshape(-1)

    sim3 = cosine_similarity(latent_df, v3).reshape(-1)
    sim4 = cosine_similarity(latent_df_2, v4).reshape(-1)

    hybrid_1 = ((sim1 + sim2)/2.0)
    hybrid_2 = ((sim3 + sim4)/2.0)
    hybrid_3 = ((hybrid_1 + hybrid_2)/2.0)

    dictDf = {'content': sim1 , 'collaborative': sim2, 'hybrid': hybrid_3}
    recommendation_df = pd.DataFrame(dictDf, index = latent_df.index).reset_index()
    recommendation_df.sort_values('hybrid', ascending=False, inplace=True)
    recommendation_df.rename(columns={'index': 'title'},inplace=True, errors='raise')
    showtime_df = recommendation_df.iloc[2:]

    return showtime_df['title'].head(50)
