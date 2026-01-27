import streamlit as st
from transformers import pipeline
from utils.database import create_table

#--------Config page ---------#
st.set_page_config(page_title= "Thinking out loud" , layout ="centered")
create_table()


#------------Title --------------#
st.title("Thinking out loud")
st.text("Hi , I am  Manasa!")


#----------------Load AI Model------------#
#loads a pretrained NLP model that knows how to read long text and generate summary
@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        device = -1
    )

summarizer = load_summarizer()


#-----------------helper functions -----------------------#
#blog goes into the model and model finds important sentences and rewrites concisely
def generate_summary(text):
    summary = summarizer(
        text,
        max_length=80,     #keeps it 3-5 lines
        min_length=40,     #avoids tiny useless summaries
        do_sample=False       #stable output (same input -> same result)
    )
    return summary[0]["summary_text"]


#----------------Navigation of Pages ---------#
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






