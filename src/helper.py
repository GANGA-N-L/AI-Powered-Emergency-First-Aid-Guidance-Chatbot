import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


#Loading the pdfs
def load_pdf_data(data_path="Data"):
    documents=[]

    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            print(f"Loading {file}...")
            loader=PyPDFLoader(os.path.join(data_path,file))
            docs=loader.load()
            documents.extend(docs)

    return documents


#Cleaning the documents
def clean_loaded_documents(documents):
    cleaned_docs=[]

    for doc in documents:
        #Keep only important metadata
        new_metadata={
            "source":doc.metadata.get("source")
        }

        cleaned_doc=Document(
            page_content=doc.page_content,
            metadata=new_metadata
        )

        cleaned_docs.append(cleaned_doc)

    return cleaned_docs



#Chunking the loaded text
def split_documents(cleaned_docs):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,           #precision
        chunk_overlap=100         #context retention
    )

    chunks=text_splitter.split_documents(cleaned_docs)
    return chunks



#Download the embedding model from HuggingFace
def create_embedding_model():
    embedding_model=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model