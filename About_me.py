import streamlit as st

#st.image("me.png")


import streamlit as st

# Create two columns
col1, col2 = st.columns([3, 1])  # left wider, right narrower

with col1:
    st.write("""
    
    
    """)

with col2:
    st.image("images/me.png", use_container_width=True)
