import streamlit as st
from utils.database import create_table
create_table()

st.title("Thinking out loud")
st.text("Hi , I am  Manasa!")

pages = {
    "About me": [
        st.Page("About_me.py", title="About me"),
    ],
    "Blogs": [
        st.Page("Projects.py", title="Projects I am working on"),
        st.Page("travel.py", title="Places I've been to"),
        st.Page("life.py" , title = "Reflections on Life"),
        st.Page("arts.py" , title = "Dance and music"),
        st.Page("write_blog.py" , title = "Write a Blog")
    ],
}

pg = st.navigation(pages)
pg.run()

def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)

