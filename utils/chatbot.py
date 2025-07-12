from utils.vector_store import search_similar_chunks
from langchain.llms import Ollama

llm = Ollama(model="gemma3:4b")

def ask_question(query):
    context = "\n".join(search_similar_chunks(query))
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return llm(prompt)