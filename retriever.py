import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatIP(dim)
        self.texts = []
        self.metadatas = []

    def _normalize(self, vectors):
        return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)

    def add(self, embeddings, texts, metadatas):
        embeddings = np.array(embeddings).astype('float32')
        embeddings = self._normalize(embeddings)

        self.index.add(embeddings)
        self.texts.extend(texts)
        self.metadatas.extend(metadatas)

    def search(self, query_embedding, k=3, threshold=0.4):
        query_embedding = np.array([query_embedding]).astype('float32')
        query_embedding = self._normalize(query_embedding)

        D, I = self.index.search(query_embedding, k)

        results = []
        seen_pages = set()

        for score, idx in zip(D[0], I[0]):
            if score < threshold:
                continue

            page = self.metadatas[idx].get("page", "Unknown")

            if page not in seen_pages:
                seen_pages.add(page)

                results.append({
                    "text": self.texts[idx],
                    "page": page,
                    "score": float(score)
                })

        return results