import streamlit as st
import plotly.express as px
from movies.service import MovieService

def show_home():
    movie_service = MovieService()
    try:
        movie_stats = movie_service.get_movie_stats() or {}
    except Exception as e:
        st.error(f'Erro ao carregar estatísticas: {e}')
        return

    st.title('Estatísticas de Filmes')

    movies_by_genre = movie_stats.get('movies_by_genre') or []
    if isinstance(movies_by_genre, dict) and 'results' in movies_by_genre:
        movies_by_genre = movies_by_genre['results'] or []

    if movies_by_genre:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movies_by_genre,
            values='count',
            names='genre__name',
            title='Filmes por Gênero',
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info('Sem dados de gêneros ainda.')

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_stats.get('total_movies', 0))

    st.subheader('Total de Avaliações Cadastradas:')
    st.write(movie_stats.get('total_reviews', 0))

    st.subheader('Média Geral de Estrelas nas Avaliações:')
    st.write(movie_stats.get('average_stars', 0))
