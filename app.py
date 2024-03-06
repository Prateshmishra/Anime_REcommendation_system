import pickle
import streamlit as st

def recommend(anime, anime_name):
    index = anime[anime['name'] == anime_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(anime.iloc[i[0]]['name'])
    return recommended_movie_names


st.header('Anime Recommender System')
anime = pickle.load(open('C:\Flask projects\Anime Streaming & Recommendation Platform/anime_list.pkl','rb'))
similarity = pickle.load(open('C:\Flask projects\Anime Streaming & Recommendation Platform/similarity.pkl','rb'))

movie_list = anime['name'].values
selected_anime = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)
if st.button('Show Recommendation'):
    recommended_anime_names = recommend(anime, selected_anime)
    st.write("Recommended Anime:")
    for recommended_anime in recommended_anime_names:
        st.write(recommended_anime)
    
