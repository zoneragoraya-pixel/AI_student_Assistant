from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_embeddings_from_text(text):
    chunks = text.split(". ")

    vectors = []
    for c in chunks:
        if len(c.strip()) > 5:
            vec = model.encode(c)
            vectors.append((c, vec))

    return vectors