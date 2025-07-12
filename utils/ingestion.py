from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from config import VECTOR_DB_DIR

chroma_client = chromadb.Client(Settings(persist_directory=VECTOR_DB_DIR))
collection = chroma_client.get_or_create_collection("study_content")
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_and_store(text):
    chunks = [text[i:i+512] for i in range(0, len(text), 512)]
    embeddings = model.encode(chunks)
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    collection.add(documents=chunks, embeddings=embeddings, ids=ids)