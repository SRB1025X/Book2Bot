from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from config import VECTOR_DB_DIR

model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.Client(Settings(persist_directory=VECTOR_DB_DIR))
collection = chroma_client.get_or_create_collection("study_content")

def search_similar_chunks(query):
    query_embedding = model.encode([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=5)
    return results["documents"][0]