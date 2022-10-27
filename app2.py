import streamlit as st
from recomender2 import *
from PIL import Image

st.set_page_config(
   page_title="movie buddy",
   page_icon="📽️",
   layout="centered",
   initial_sidebar_state="expanded",
)


'''
# Movie Buddy
##### Find the perfect movies to watch together

'''
st.markdown("It's movie night and the question comes up again: 'Which movie should we watch?'. Worry no more, this app will make your life easier! Just search for two movies and the app will return the best recommendations you both will enjoy.")




col1, col2 = st.columns(2)


with col1:
    option_1 = st.selectbox('Search for a great movie', (movies['title']), key='first_choice', index=7400 )
    # st.write('You selected:', option_1)

with col2:
    option_2 = st.selectbox('Search for another great movie', (movies['title']), key='second_choice', index=8358 )
    # st.write('You selected:', option_2)

df = recommend(option_1,option_2)

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Display a static table
if st.button('Find Movies'):
    st.markdown("Some recommendations you will love:", unsafe_allow_html=False)
    st.table(df)
