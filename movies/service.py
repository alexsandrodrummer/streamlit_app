import streamlit as st
import datetime
from movies.repository import MovieRepository

class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies 
        return movies 

    def create_movie(self, title, release_date, genre, actors, resume):
        # Garante formato de data ISO (YYYY-MM-DD)
        if isinstance(release_date, (datetime.date, datetime.datetime)):
            release_date = release_date.date().isoformat() if isinstance(release_date, datetime.datetime) else release_date.isoformat()
        elif isinstance(release_date, str):
            release_date = release_date.strip()  
        else:
            release_date = str(release_date)

        payload = {
            "title": (title or "").strip(),
            "release_date": release_date,
            "genre": genre,         
            "actors": actors,       
            "resume": resume,       
        }
        new_movie = self.movie_repository.create_movie(payload)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        return self.movie_repository.get_movies_stats()




# from movies.repository import MovieRepository
# import streamlit as st

# class MovieService:

#     def __init__(self):
#         self.movie_repository =  MovieRepository()
    
#     def get_movies(self):
#         if 'movies' in st.session_state:
#             return st.session_state.movies
#         movies = self.movie_repository.get_movies()
#         st.session_state.movies = movies

#         return movies
    
#     def create_movie(self, title, release_date, genre, actors, resume):
#         movie = dict(
#             title=title,
#             release_date=release_date,
#             genre=genre,
#             actor=actors,
#             resume=resume,
#         )
#         return self.movie_repository.create_movie(movie) 
