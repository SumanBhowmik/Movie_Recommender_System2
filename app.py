import streamlit as st
import pickle
import pandas as pd

import gdown
import os

# Google Drive file ID
file_id = '1Hq9HEyVjX-3yKPe4VOArNfosGI4Udxnh'
output = 'similarity.pkl'

# Construct the download URL
url = f'https://drive.google.com/uc?id={file_id}'

# Check if the file already exists before downloading
if not os.path.exists(output):
    print(f"Downloading {output} from Google Drive...")
    gdown.download(url, output, quiet=False)
    print(f"Downloaded {output} successfully.")
else:
    print(f"{output} already exists. No need to download.")


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recomender System')


selected_movie_name = st.selectbox('Search your Movie here',movies['title'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
