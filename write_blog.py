import streamlit as st
from utils.database import insert_blog
from utils.nlp_utils import suggest_category, CATEGORIES
from app import generate_summary


#------Frontend UI----------------------#
st.title("What's on your mind today?")
title = st.text_input("Blog Title")
content = st.text_area("Blog Content", height= 300)

#----------------AI Category suggestion-------#
if content.strip():
  suggested_category, confidence = suggest_category(content)
  st.info(
        f" Suggested Category: **{suggested_category}** "
        f"(confidence: {confidence:.2f})"
    )
  final_category = st.selectbox(
        "Choose Category",
        options=CATEGORIES,
        index=CATEGORIES.index(suggested_category)
    )
  st.subheader(" AI Summary")
  if "summary" not in st.session_state:
     st.session_state["summary"] = ""
  if st.button("Generate summary"):
      st.session_state["summary"]=generate_summary(content)

  summary_text = st.text_area(
        "Edit your summary (3–5 lines):",
        value=st.session_state["summary"],
        height=150
    )
  

  #------------Export options----------#
  st.subheader("📤 Export Summary")
  st.download_button(
        "Download as Markdown",
        f"### Blog Summary\n\n{summary_text}",
        file_name="summary.md"
    )
  st.download_button(
        "Download as Plain Text",
        summary_text,
        file_name="summary.txt"
    )
  
  #----------Publish ------------_#
  if st.button("Publish"):
        if title.strip():
            insert_blog(title, content, final_category)
            st.success("Blog published successfully!")
        else:
            st.error("Title cannot be empty")

   

    

    

    

    

