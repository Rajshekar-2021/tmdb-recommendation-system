# TMDB-MOVIE Recommendation-system

This repository has content based movie recommendation  system



### Steps involved in this Project:

- We have extracted the Original Dataset from TMDB - Website using API's 
- The below `features` were collected :
         
        1. `Movie_id`, 
        2. `Title`, 
        3. `Keywords`, 
        4. `Genre`, 
        5. `Top 5 popular cast based on Popularity`, 
        6. `Director` and 
        7.  The `Overview`
         
- The features are cleaned for extra spaces, special charecters, and converted into lower case charecters
- Created a new column `tags` with all the charecters in different features
- By using NLP Techniques:
       
       1. Removal of stop words, Stemming and Converting strings into Vectors. 
       
       2. Here we have used `CountVectorizer`, and we could have used `tf-idf`, however we do not the actual liguistic meaning of the words
       
       3. Similarity between the vecors is checked by implementing `cosine_similarity` function
       
       4. Arranged the vectors in descending order to get the top 5 most similar movies
       
- Saved the Movies Dataframe and Similarity matrix into pickle files, to further use it in `pycharm` to build streamlit web app 


[click here to see the Demo app - streamlit](https://share.streamlit.io/rajshekar-2021/tmdb-recommendation-system/main/tmdb-app-final.py)


### The below is the screen shot of the app developed using Streamlit

![](https://github.com/Rajshekar-2021/tmdb-recommendation-system/blob/main/Demo%20Screen%20Shot.png)

