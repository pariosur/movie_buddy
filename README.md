# Movie Buddy
> It's movie night and the question comes up again: "Which movie should we watch?". Worry no more, this app will make your life easier!
> Just pick two movies and the app will return the best recommendations for both. 
> 
> Live demo [_here_](https://movie-buddy.streamlitapp.com/)

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)


## General Information
- The recommendation system works as a hybrid model.
- It uses **content-based** based on similarity of movie attributes: genre, actors, and other descriptive metadata associated with a movie. And **collaborative filtering** based on user ratings from the [_movieLens_](https://grouplens.org/datasets/movielens/) dataset .  
- Both attributes and ratings were transformed into vectors in order to create a latent factor model with the best features. Those that explain at least 80% of the variance.
- Then used cosine similarity as a similarity measure to find the most similar movies for each of the user choices.
- Lastly, a global measure average for both movies was calculated for both content and collaborative.  

## Technologies Used
- Python
- Streamlit 
- Scikit-learn


