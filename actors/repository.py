import requests 
import streamlit as st
from login.service import logout

class ActorRepository:
    def __init__(self):
        self.__base_url = 'https://alexsandro31.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'

    def get_headers(self):
        if "token" not in st.session_state:
            logout()
        return {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.get_headers()
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.get_headers(),
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao cadastrar dados na API. Status code: {response.status_code}')
