from sentence_transformers import SentenceTransformer

def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    """
    Loads a sentence transformer model for generating embeddings.
    """
    model = SentenceTransformer(model_name)
    return model