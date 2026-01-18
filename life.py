import streamlit as st
from utils.database import get_connection , delete_blog
from utils.database import get_blogs_by_category

st.title("Reflections on Life")

blogs = get_blogs_by_category("Personal Life")

for blog in blogs:
    st.subheader(blog[1])
    st.write(blog[2])
    st.caption(blog[3])

conn = get_connection()
c = conn.cursor() 

c.execute("SELECT id , title , content , date FROM blogs WHERE category = 'Life' ORDER BY date DESC")
blogs = c.fetchall()


for blog_id, title, content, date in blogs:
    st.subheader(title)
    st.caption(date)
    st.write(content)

    col1, col2 = st.columns([1, 5])

    with col1:
        if st.button("🗑 Delete", key=f"delete_{blog_id}"):
            delete_blog(blog_id)
            st.success("Blog deleted successfully!")
            st.rerun()

    st.divider()

