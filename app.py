import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()

embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = Chroma(persist_directory="embedding/chroma_db", embedding_function=embedding_function)

class LocalChatOpenAI(ChatOpenAI):
    def __init__(self, **kwargs):
        super().__init__(
            openai_api_base="http://127.0.0.1:1234/v1",
            openai_api_key="not-needed",
            model="meta-llama-3-8b-instruct",
            **kwargs
        )

llm = LocalChatOpenAI()

st.title("💬 Philips AI FAQ Chatbot")

retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = st.text_input("Ask your question here:")

if query:
    answer = qa.run(query)
    st.write("🤖", answer)