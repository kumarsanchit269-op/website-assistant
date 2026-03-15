from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma

from config import CHUNK_SIZE, CHUNK_OVERLAP, LLM_MODEL, EMBEDDING_MODEL


def create_vector_store(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    docs = splitter.create_documents([text])

    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    vector_store = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="vector_store"
    )

    return vector_store


def ask_question(vector_store, question):

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k":4}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI(
        model=LLM_MODEL,
        temperature=0
    )

    prompt = f"""
Answer the question using the provided website content.

Context:
{context}

Question:
{question}

Answer clearly.
"""

    response = llm.invoke(prompt)

    return response.content