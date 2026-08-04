# Vector Search is database; it's gonna be hosted locally on our own computer using somethin called ChromaDB
# quickly look up relevant information that we can then pass to our model (contexttually relevant replies)
import os

import pandas as pd
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import (
    OllamaEmbeddings,  # embedding model is gonna take text and turn into a vector
)

df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"], # what we're gonna be vectorizing and will be looking up / any of the content that you want to use look up the information in the database (important information u gonna be querying on)
            metadata = {"rating": row["Rating"], "date": row["Date"]},  # additional information we gonna be grabing along with the document
            id= str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name = "restaurant_reviews",
    persist_directory =db_location,
    embedding_function = embeddings
)

if add_documents:
    vector_store.add_documents(documents= documents, ids= ids)

# Making the vector store be used to the LLM / Connecting LLM & Vector Store
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5} # number of documents to look for / looking 5 reviews and passing to the llm
)