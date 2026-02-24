from flask import Flask, render_template, request, jsonify
from src.helper import create_embedding_model
from langchain_pinecone import PineconeVectorStore
from langchain_community.chat_models import ChatOllama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


#Initializing Flask
app = Flask(__name__)


load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")

embedding_model=create_embedding_model()

index_name="aiemergencyfirstaidchatbot"

vector_store=PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding_model
)


retriever=vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":3}
)


llm=ChatOllama(
    model="phi",
    temperature=0               #more factual answers
)


custom_prompt=PromptTemplate(
    input_variables=["context","input"],
    template="""
You are an AI assistant specialized in emergency first aid guidance.
Answer the question ONLY using the information provided in the context below.
If the answer is not found in the context,say:
"I don't have enough information in my knowledge base."

Using ONLY the provided context, answer the question.

Provide:
1. Step-by-step first aid instructions.
2. A separate section titled "Do NOT".
3. Use numbered points.
4. Do not include information not present in the context.


Do NOT use outside knowledge.
Do NOT make assumptions.

Context:
{context}

Question:
{input}

Answer:
"""
)

document_chain=create_stuff_documents_chain(
    llm,
    custom_prompt
)


rag_chain=create_retrieval_chain(
    retriever,
    document_chain
)


#Creating the default route
@app.route("/")
def home():
    return render_template("index.html")





@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data["message"]

    response = rag_chain.invoke({"input": user_message})

    print(response["context"])

    return jsonify({
        "answer": response.get("answer", "No response generated.")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)