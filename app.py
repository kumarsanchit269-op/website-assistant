import os
import streamlit as st
from dotenv import load_dotenv

from crawler import crawl_website
from rag_pipeline import create_vector_store, ask_question

load_dotenv()

if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(
page_title="Website RAG Assistant",
page_icon="🌐"
)

st.title("🌐 Website RAG Assistant")

url = st.text_input("Enter Website URL")

if st.button("Index Website"):

    if not url:
        st.warning("Please enter a website URL.")
    else:

        with st.spinner("Crawling website..."):

            text = crawl_website(url)

            st.session_state.vector_store = create_vector_store(text)

        st.success("Website indexed successfully!")

question = st.text_input(
"Ask a question about the website"
)

if (
question
and "vector_store" in st.session_state
):

    with st.spinner("Generating answer..."):

        answer = ask_question(
            st.session_state.vector_store,
            question
        )

    st.subheader("Answer")
    st.write(answer)
