from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

from config import (
CHUNK_SIZE,
CHUNK_OVERLAP,
LLM_MODEL,
EMBEDDING_MODEL
)

def create_vector_store(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    docs = splitter.create_documents([text])

    embeddings = OpenAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    vector_store = FAISS.from_documents(
        docs,
        embeddings
    )

    return vector_store

def ask_question(vector_store, question):
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = ChatOpenAI(
        model=LLM_MODEL,
        temperature=0
    )

    prompt = f"""
    ```
    
    You are an AI assistant answering questions based only on the provided website content.
    
    If the answer is not present in the context, say:
    "I could not find that information on the indexed website."
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    """
    response = llm.invoke(prompt)

    return response.content
