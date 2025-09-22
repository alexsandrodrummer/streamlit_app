import requests
import streamlit as st

class ReviewRepository:
    def __init__(self):
        self._base_url = "https://alexsandro31.pythonanywhere.com/api/v1/"
        self._reviews_url = f"{self._base_url}reviews/"

    @property
    def headers(self):
        # Gera sempre com o token atual do Streamlit
        return {
            "Authorization": f"Bearer {st.session_state.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def list_reviews(self, params=None):
        resp = requests.get(self._reviews_url, headers=self.headers, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()

    def create_review(self, review: dict):
        resp = requests.post(self._reviews_url, headers=self.headers, json=review, timeout=15)
        if resp.status_code in (200, 201):
            return resp.json()
        # Mostra detalhes do DRF
        try:
            detail = resp.json()
        except ValueError:
            detail = resp.text
        raise Exception(f"Erro ao criar review. Status code: {resp.status_code}. Detalhes: {detail}")


# import requests
# from login.service import logout
# import streamlit as st

# class ReviewRepository:

#     def __init__(self):
#         self.__base_url = 'https://alexsandro31.pythonanywhere.com/api/v1/'
#         self.__reviews_url = f'{self.__base_url}reviews/'
#         self.__headers = {
#             'Authorization': f'Bearer {st.session_state.token}'
#         }
    
#     def get_reviews(self):
#         response = requests.get(
#             self.__reviews_url,
#             headers=self.__headers,
#         )
#         if response.status_code == 200:
#             return response.json()
#         if response.status_code == 401:
#             logout()
#             return None
#         raise Exception(f'Erro ao obter dados da API. Status code:{response.status_code}')
    
#     def create_review(self, review):
#         response = requests.post(
#             self.__reviews_url,
#             headers=self._headers,
#             data=review,
#         )
#         if response.status_code == 201:
#             return response.json()
#         if response.status_code == 401:
#             logout()
#             return None
#         raise Exception(f'Erro ao obter dados da API. Status code:{response.status_code}')