import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_dim):
        """
        Initializes a FAISS index for storing embeddings.
        """
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.text_chunks = []

    def add_embeddings(self, embeddings, chunks):
        """
        Adds embeddings and corresponding text chunks to the index.
        """
        self.index.add(np.array(embeddings).astype("float32"))
        self.text_chunks.extend(chunks)

    def search(self, query_embedding, top_k=5):
        """
        Searches the index for top_k similar embeddings.
        """
        query_embedding = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_embedding, top_k)
        results = [self.text_chunks[i] for i in indices[0]]
        return results