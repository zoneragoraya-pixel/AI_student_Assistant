def get_embeddings(text_chunks):
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
        return model.encode(text_chunks)
    except Exception:
        # Fallback to random embeddings for testing
        import warnings
        warnings.warn("Using random embeddings as fallback. This is not recommended for production.")
        import numpy as np
        return np.random.rand(len(text_chunks), 384)
