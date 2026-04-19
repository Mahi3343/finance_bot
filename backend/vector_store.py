import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection("finance_docs")

model = SentenceTransformer("all-MiniLM-L6-v2")


def store_document(text):
    chunks = text.split("\n")

    for i, chunk in enumerate(chunks):
        if chunk.strip():
            embedding = model.encode(chunk).tolist()

            collection.add(
                ids=[str(i)],
                documents=[chunk],
                embeddings=[embedding]
            )


def search_document(query):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results["documents"][0]