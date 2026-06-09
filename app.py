import streamlit as st
import pandas as pd
import pickle
import requests
from streamlit import button


# import requests

def fetch_poster(movie_id):
    try:
        api_key = "3168a5323b8d542e72ff25d5f176b062"

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

        response = requests.get(url, timeout=20)

        data = response.json()

        if 'poster_path' not in data:
            print("TMDB Response:", data)
            return None

        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    except Exception as e:
        print("Fetch Error:", e)
        return None




# movies_list=pickle.load(open('movie_dict.pkl','rb'))
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters


import lzma
# import pickle

with lzma.open("similarity_float32.lzma", "rb") as f:
    similarity = pickle.load(f)
print(similarity.shape)
print(similarity.dtype)
st.title('Movie Recommendation System')
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
print(movies.columns)
print(movies[['movie_id','title']].head())
selected_movie_name =  st.selectbox(
    'select a movie to recommend',
movies['title'].values)

#button

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.beta_columns(5)

    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0])

    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1])

    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2])

    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3])

    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4])