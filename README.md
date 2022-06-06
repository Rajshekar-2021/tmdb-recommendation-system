# tmdb-recommendation-system

This repository has content based movie recommendation  system



### Steps involved in this Project:

- We have extracted the Original Dataset from TMDB - Website using API's 
- The below `features` were collected :
         Movie_id, Title, Keywords, Genre, Top 5 popular cast based on Popularity, Director and the Overview
- The features are cleaned for extra spaces, special charecters, and converted into lower case charecters
- Created a new column `tags` with all the charecters in different features
- By using NLP Techniques:
       1. Removal of stop words, Stemming and Converting strings into Vectors. 
       2. Here we have used `CountVectorizer`, and we could have used `tf-idf`, however we do not the actual liguistic meaning of the words
       - Similarity between the vecors is checked by implementing `cosine_similarity` function
       - Arranged the vectors in descending order to get the top 5 most similar movies
- Saved the Movies Dataframe and Similarity matrix into pickle files, to further use it in `pycharm` to build streamlit web app 


[click here to see the Demo app - streamlit](https://share.streamlit.io/rajshekar-2021/tmdb-recommendation-system/main/tmdb-app-final.py)

