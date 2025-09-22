import streamlit as st
from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_respository = ActorRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actor_respository.get_actors()
        st.session_state.actors = actors
        return actors
    
    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthda=birthday,
            nationality=nationality,
        ) 
        new_actor = self.actor_respository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor