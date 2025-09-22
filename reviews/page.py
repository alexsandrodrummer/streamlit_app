import pandas as pd
import streamlit as st
from movies.service import MovieService
from st_aggrid import AgGrid
from reviews.service import ReviewService

def _to_list(data):
    # Aceita tanto {"results":[...]} quanto [...]
    if isinstance(data, dict) and "results" in data:
        return data["results"] or []
    return data or []

def show_reviews():
    review_service = ReviewService()

    # --- Lista de avaliações
    try:
        reviews = _to_list(review_service.get_reviews())
    except Exception as e:
        reviews = []
        st.error(f"Erro ao carregar avaliações: {e}")

    if reviews:
        st.write("Lista de avaliações:")
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            reviews_df,
            reload_data=True,
            key="reviews_grid",
        )
    else:
        st.warning("Nenhuma avaliação encontrada.")

    st.title("Cadastrar nova avaliação")

    # --- Filmes para selecionar
    movie_service = MovieService()
    try:
        movies = _to_list(movie_service.get_movies())
    except Exception as e:
        movies = []
        st.error(f"Erro ao carregar filmes: {e}")

    if not movies:
        st.info("Não há filmes disponíveis para avaliar.")
        return

    movie_titles = {movie["title"]: movie["id"] for movie in movies}
    selected_movie_title = st.selectbox("Filme", list(movie_titles.keys()))

    # ⭐ No mínimo 1, no máximo 5
    stars = st.number_input(
        label="Estrelas",
        min_value=1,
        max_value=5,
        step=1,
        value=5,  # default agradável
    )

    comment = st.text_area("Comentário")

    if st.button("Cadastrar"):
        try:
            new_review = review_service.create_review(
                movie=movie_titles[selected_movie_title],  # ID
                stars=int(stars),
                comment=comment,
            )
            st.success("Review criada com sucesso!")
            st.json(new_review)
            st.rerun()
        except Exception as e:
            # Vai exibir detalhes do DRF vindos do raise do repository
            st.error(str(e))



# import pandas as pd
# import streamlit as st
# from movies.service import MovieService
# from st_aggrid import AgGrid
# from reviews.service import ReviewService

# def show_reviews():
#     review_service = ReviewService()
#     reviews = review_service.get_reviews()

#     if reviews:
#         st.write('Lista de avaliações:')

#         reviews_df = pd.json_normalize(reviews)
#         AgGrid(
#             data=reviews_df,
#             reload_data=True,
#             key='reviews_grid',
#         )
#     else:
#         st.warning('Nenhuma avaliação encontrada.')
    
#     st. title('Cadastrar nova avaliação')

#     movie_service = MovieService()
#     movies = movie_service.get_movies()

#     movie_titles = {movie['title']: movie['id'] for movie in movies}
#     selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))


#     stars = st.number_input(
#         label='Estrelas',
#         min_value=0,
#         max_value=5,
#         step=1,
#     )
#     comment = st.text_area('Comentário')

#     if st.button('Cadastrar'):
#         new_review = review_service.create_review(
#             movie=movie_titles[selected_movie_title],
#             stars=stars,
#             comment=comment,
#         )
#         if new_review:
#             st.rerun()
#         else:
#             st.error('Erro ao cadastrar a avaliação. Verifique os campos')