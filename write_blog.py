import streamlit as st
from datetime import date
from utils.database import get_connection

#Frontend UI
st.title("What's on your mind today?")

title = st.text_input("Blog Title")

content = st.text_area("Blog Content", height=200)

category = st.selectbox(
    "Select Category",
    ["Life", "Travel", "Projects", "Arts"]
)

blog_date = st.date_input("Date", value=date.today())

submit = st.button("Publish")


#Backend - Database part
if submit:
  if title and content:
    conn = get_connection()          #establish a connection
    c = conn.cursor()                 # cursor object to execute SQL queries

    c.execute(
      "INSERT into blogs (title , content , category , date) VALUES (? , ? , ? , ?)" , 
      (title , content , category , str(blog_date))      #name of the variable created above
    )

    conn.commit()
    conn.close()

    st.success(" Yay! Blog published")
  else:
    st.error("Title and content cannot be empty")

