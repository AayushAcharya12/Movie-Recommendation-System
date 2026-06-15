import streamlit as st
import pickle
import requests
import joblib


# Load files
movies=joblib.load('../models/movies.pkl')
similarity=joblib.load('../models/similarity.pkl')

#TMDB API key
API_KEY = "46cb873181bc7ca2b7a33f4199b10ba2"



def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        data = requests.get(url, timeout=5).json()
        path = data.get("poster_path")
        if path:
            return f"https://image.tmdb.org/t/p/w500{path}"
    except Exception:
        pass
    # fallback placeholder
    return "https://via.placeholder.com/500x750?text=No+Poster"
 
# Recommend function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[0:6]



    recommended_movies = []
    recommended_posters = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append( movies.iloc[i[0]].title)

        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_posters


# Streamlit UI
st.title("Movie Recommendation System")

selected_movie = st.selectbox("Select Movie", movies['title'].values)

if st.button("Search"):

    names, posters = recommend(selected_movie)

    st.subheader("Selected Movie")
    st.write(selected_movie)
    st.image(posters[0], width=120)

    st.subheader("Recommended Movies")

    cols = st.columns(5)
    j = 0
    for i in range(len(names)):
        if names[i] == selected_movie:
            continue
        with cols[j]:
            st.text(names[i])
            st.image(posters[i], width=120)
        j += 1
        if j == 5:
            break