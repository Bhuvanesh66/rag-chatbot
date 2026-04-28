from sentence_transformers import SentenceTransformer

def load_embedding_model():
    # ✅ multilingual support
    return SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def embed_texts(model, texts, batch_size=32):
    return model.encode(texts, batch_size=batch_size, show_progress_bar=True)