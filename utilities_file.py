import pickle
import requests
import tmdb_api_key

api_key = tmdb_api_key.api_key
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend_movies(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    recommended_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[:6]

    movies_with_id =[]
    movie_names=[]
    for i in recommended_movies[1:]:
        movies_with_id.append(movies.iloc[i[0],:]['movie_id'])
        movie_names.append(movies.iloc[i[0],:]['title'])


    posters_url = []

    for id in movies_with_id:
        poster = fetch_movie_poster(id)
        posters_url.append(poster)

    return movie_names,posters_url


def fetch_movie_poster(movie_id):
    url = ('https://api.themoviedb.org/3/movie/{}?api_key='+api_key+'&language=en-US').format(movie_id)
    response_url = requests.get(url).json()
    response_url['poster_path']

    poster = "https://image.tmdb.org/t/p/w500"+response_url['poster_path']

    return poster

