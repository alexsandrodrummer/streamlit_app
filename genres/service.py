import streamlit as st
from genres.repository import GenreRepository


class GenreService:

    def __init__(self):
        self.genre_repository = GenreRepository()
    
    def get_genres(self):
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.genre_repository.get_genres()
        st.session_state.genres = genres  
        return genres 
    
    #metodo de exemplo que retorna apenas uma lista de string 
#    def get_genre_name(self):
#        genres = self.genre_respository.get_genres()
#        genre_names = list()
#        for genre in genres:
#            genre_names.append(genre.get('name'))
#        return genre_names
    
    def create_genre(self, name):
        genre = dict(
            name=name,

        )
        new_genre = self.genre_repository.create_genre(genre)
        st.session_state.genres.append(new_genre) 
        return new_genre

