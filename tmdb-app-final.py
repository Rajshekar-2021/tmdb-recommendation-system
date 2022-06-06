import streamlit as st
import pandas as pd
import pickle
import tmdb_api_key

import utilities_file
api_key = tmdb_api_key.api_key

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


st.markdown("# TMDB-Movie Recommendation")

option = st.selectbox("Select the Movie", movies['title'].values)

if st.button("Click Here - To get Recommnded Movies") :
    movies_name,posters_url = utilities_file.recommend_movies(option)

    col1,col2,col3,col4,col5 = st.columns(5)

    i = 0
    for col in st.columns(5):
        with col :
            # st.header(movies_name[i])
            st.image(posters_url[i])
            i+=1

