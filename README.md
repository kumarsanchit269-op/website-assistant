# Website Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to ask questions about the content of any website. The system crawls a webpage, processes its content, stores embeddings in a vector database, and generates context-aware answers using a Large Language Model (LLM).

---

## Features

- Extracts content from websites
- Converts website content into semantic embeddings
- Stores embeddings in a vector database
- Retrieves relevant content using semantic search
- Generates accurate answers using an LLM
- Interactive user interface built with Streamlit

---

## Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI API
- Chroma Vector Database
- BeautifulSoup (Web scraping)

---

## How It Works

The system follows a Retrieval-Augmented Generation (RAG) pipeline:

Website URL
↓
Web scraping
↓
Text chunking
↓
Embeddings generation
↓
Vector database storage
↓
Semantic retrieval
↓
LLM generates answer


---

## Project Structure


website-rag-assistant
│
├── app.py # Streamlit interface
├── crawler.py # Website content extraction
├── rag_pipeline.py # RAG pipeline logic
├── config.py # Configuration settings
├── requirements.txt # Project dependencies
├── README.md
│
└── vector_store/ # Stored embeddings


---

## Installation

Clone the repository

git clone https://github.com/kumarsanchit269-op/website-assistant.git


# In terminal:

cd website-assistant

-> Create a virtual environment

python -m venv venv


-> Activate the environment

Windows

venv\Scripts\activate


# Install dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a `.env` file in the project root:


OPENAI_API_KEY=your_api_key_here


---

## Run the Application

streamlit run app.py


Open in browser:


http://localhost:8501


---

## Example Usage

1. Enter a website URL
2. The system crawls and processes the website
3. Ask questions about the website content
4. The AI generates answers using the extracted knowledge

Example:


URL: https://docs.python.org

Question: What are Python lists?


---

## Future Improvements

- Multi-page website crawling
- Support for multiple URLs
- Chat-style conversational interface
- Deployment to cloud platforms

---

## Author

Sanchit Kumar  
AI/ML Student | Aspiring AI Engineer