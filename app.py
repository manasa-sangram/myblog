import streamlit as st

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
        st.Page("arts.py" , title = "Dance and music")
    ],
}

pg = st.navigation(pages)
pg.run()

def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)