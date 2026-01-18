import streamlit as st
from datetime import date
from utils.database import get_connection
from utils.database import insert_blog
from utils.nlp_utils import suggest_category, CATEGORIES


#Frontend UI
st.title("What's on your mind today?")

title = st.text_input("Blog Title")

content = st.text_area("Blog Content", height= 300)

#Manual Category selector
# category = st.selectbox(
#     "Select Category",
#     ["Life", "Travel", "Projects", "Arts"]
# )

# blog_date = st.date_input("Date", value=date.today())

# submit = st.button("Publish")

if content.strip():
  suggested_category, confidence = suggest_category(content)

  st.info(
        f"🤖 Suggested Category: **{suggested_category}** "
        f"(confidence: {confidence:.2f})"
    )

    # User can accept or override
  final_category = st.selectbox(
        "Choose Category",
        options=CATEGORIES,
        index=CATEGORIES.index(suggested_category)
    )

    # SINGLE publish button
  if st.button("Publish"):
      if title.strip():
            insert_blog(title, content, final_category)
            st.success("✅ Blog published successfully!")
      else:
            st.error("❌ Title cannot be empty")


#Backend - Database part
# if submit:
#   if title and content:
#     conn = get_connection()          #establish a connection
#     c = conn.cursor()                 # cursor object to execute SQL queries

#     c.execute(
#       "INSERT into blogs (title , content , category , date) VALUES (? , ? , ? , ?)" , 
#       (title , content , category , str(blog_date))      #name of the variable created above
#     )

#     conn.commit()
#     conn.close()

#     st.success(" Yay! Blog published")
#   else:
#     st.error("Title and content cannot be empty")

