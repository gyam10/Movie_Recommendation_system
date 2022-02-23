import pickle
import streamlit as str
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # for movies poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


str.header('Movie Recommender')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = str.selectbox(
    "Select or type movies name",
    movie_list
)

if str.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = str.columns(5)
    with col1:
        str.text(recommended_movie_names[0])
        str.image(recommended_movie_posters[0])
    with col2:
        str.text(recommended_movie_names[1])
        str.image(recommended_movie_posters[1])

    with col3:
        str.text(recommended_movie_names[2])
        str.image(recommended_movie_posters[2])
    with col4:
        str.text(recommended_movie_names[3])
        str.image(recommended_movie_posters[3])
    with col5:
        str.text(recommended_movie_names[4])
        str.image(recommended_movie_posters[4])
