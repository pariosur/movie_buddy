import streamlit as st
from recomender2 import *


'''
# Movie Buddy

##### Choose two movies. We'll combine them to show recommendations you'll love!

'''
# title = st.text_input('Movie title', 'Search a movie you like')


col1, col2 = st.columns(2)


with col1:
    option_1 = st.selectbox('Search a movie you like', (movies['title']), key='first_choice', index=7400 )
    # st.write('You selected:', option_1)

with col2:
    option_2 = st.selectbox('Search a movie you like', (movies['title']), key='second_choice', index=8358 )
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
st.table(df)
