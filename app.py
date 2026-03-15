import streamlit as st
from dotenv import load_dotenv

from crawler import crawl_website
from rag_pipeline import create_vector_store, ask_question

load_dotenv()

st.title("Website RAG Assistant")

url = st.text_input("Enter Website URL")

if st.button("Index Website"):

    with st.spinner("Crawling website..."):

        text = crawl_website(url)

        st.session_state.vector_store = create_vector_store(text)

        st.success("Website indexed successfully!")

question = st.text_input("Ask a question about the website")

if question and "vector_store" in st.session_state:

    answer = ask_question(st.session_state.vector_store, question)

    st.write("### Answer")
    st.write(answer)