import streamlit as st
from genres.page import show_genres
from home.page import show_home
from login.page import show_login
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews

def main():
    # Se não logado, mostra login e sai
    if 'token' not in st.session_state:
        show_login()
        return

    st.title('App Stream')

    # Padronize o texto do menu (use acento e mesma capitalização na checagem)
    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações'],
        index=0  # mostra Home por padrão
    )

    if menu_option == 'Início':
        show_home()
    elif menu_option == 'Gêneros':
        show_genres()
    elif menu_option == 'Atores/Atrizes':
        show_actors()
    elif menu_option == 'Filmes':
        show_movies()
    elif menu_option == 'Avaliações':
        show_reviews()

if __name__ == '__main__':
    main()
