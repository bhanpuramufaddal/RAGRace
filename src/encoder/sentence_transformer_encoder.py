from src.encoder.base import IEncoder

class SentenceTransformerEncoder(IEncoder):
    def __init__(self, model_name):
        super().__init__(model_name)
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name)
        
    def encode(self, text):
        return self.model.encode(text)
    
    def encode_batch(self, texts):
        return self.model.encode(texts)

    def dimension(self):
        return self.model.get_sentence_embedding_dimension()