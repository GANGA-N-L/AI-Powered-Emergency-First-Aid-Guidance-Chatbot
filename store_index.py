import os
from dotenv import load_dotenv
from src.helper import load_pdf_data,clean_loaded_documents,split_documents,create_embedding_model
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")

loaded_data=load_pdf_data("Data")
cleaned_data=clean_loaded_documents(loaded_data)
chunks=split_documents(cleaned_data)
embedding_model=create_embedding_model()

pc=Pinecone(api_key=PINECONE_API_KEY)

index_name="aiemergencyfirstaidchatbot"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  #Must match embedding model dimension
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )


vector_store=PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    index_name=index_name
)