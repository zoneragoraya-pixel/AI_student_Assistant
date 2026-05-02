import faiss
import numpy as np
# from embeddings import get_embeddings  # Lazy import

class RAG:
    def __init__(self):
        self.text_chunks = []
        self.index = None

    def add_documents(self, text):
        from embeddings import get_embeddings
        self.text_chunks = text.split("\n")
        embeddings = get_embeddings(self.text_chunks)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))

    def search(self, query):
        from embeddings import get_embeddings
        if self.index is None:
            return []  # Return empty list if no documents
        
        query_vec = get_embeddings([query])
        D, I = self.index.search(np.array(query_vec), k=3)
        return [self.text_chunks[i] for i in I[0]]

rag = RAG()