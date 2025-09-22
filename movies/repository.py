import requests
import streamlit as st
from login.service import logout
class MovieRepository:
    def __init__(self):
        self.__base_url = 'https://alexsandro31.pythonanywhere.com/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    def get_movies(self):
        resp = requests.get(self.__movies_url, headers=self.__headers, timeout=15)
        resp.raise_for_status()
        return resp.json()

    def create_movie(self, movie: dict):
        resp = requests.post(self.__movies_url, headers=self.__headers, json=movie, timeout=15)
        if resp.status_code in (200, 201):
            return resp.json()
        # <<< Mostre os detalhes vindos do DRF
        try:
            detail = resp.json()
        except ValueError:
            detail = resp.text
        raise Exception(f'Erro ao criar filme. Status code: {resp.status_code}. Detalhes: {detail}')

    def get_movies_stats(self):
        response = requests.get(
            f'{self.__movies_url}stats/',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception (f'Erro so obter dados da API, Status code:{response.status_code}')
# import requests
# import streamlit  as st
# from login.service import logout



# class MovieRepository:

#     def __init__(self):
#         self.__base_url = 'https://alexsandro31.pythonanywhere.com/api/v1/'
#         self.__movies_url = f'{self.__base_url}movies/'
#         self.__headers = {
#             'Authorization': f'Bearer {st.session_state.token}'
#         }

#     def get_movies(self):
#         response = requests.get(
#             self.__movies_url,
#             headers=self.__headers,
#         )
#         if response.status_code == 200:
#             return response.json()
#         if response.status_code == 401:
#             logout()
#             return None
#         raise Exception(f' Erro ao obter dados da API. Status code: {response.status_code}')
    
#     def create_movie(self, movie):
#         response = requests.post(
#             self.__movies_url,
#             headers=self.__headers,
#             data=movie,
#         )
#         if response.status_code == 201:
#             return response.json()
#         if response.status_code == 401:
#             logout()
#             return None
#         raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

#     def get_movie_stats(self):
#         response = requests.get(
#             f'{self.__movies_url}stats/',
#             headers=self.__headers
#         )
#         if response.status_code == 200:
#             return response.json()
#         if response.status_code == 401:
#             logout()
#             return None
#         raise Exception(f'Erro ao obter dados da API. Status code:{response.status_code}')