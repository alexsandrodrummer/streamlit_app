
import streamlit as st
from reviews.repository import ReviewRepository

class ReviewService:
    def __init__(self):
        self.review_repository = ReviewRepository()

    def list_reviews(self, params=None):
        return self.review_repository.list_reviews(params=params)

    # ✅ alias para compatibilizar com o page.py atual
    def get_reviews(self, params=None):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews = self.review_repository.list_reviews(params=params)
        st.session_state.reviews = reviews
        return reviews

    def create_review(self, movie, stars, comment):
        stars = int(stars)
        if not (1 <= stars <= 5):
            raise Exception("Stars deve ser um inteiro entre 1 e 5.")
        payload = {"movie": movie, "stars": stars, "comment": (comment or "").strip()}

        new_review = self.review_repository.create_review(payload)
        st.session_state.reviews.append(new_review) 
        return new_review





# from reviews.repository import ReviewRepository



# class ReviewService:

#     def __init__(self):
#         self.review_repository = ReviewRepository()

#     def get_reviews(self):
#         return self.review_repository.get_reviews()
    
#     def create_review(self, movie, stars, comment):
#         review = dict(
#             movie=movie,
#             stars=stars,
#             comment=comment,
#         )
#         return self.review_repository.create_review(review)