from dspy import Prediction
from dsp.utils import dotdict
from typing import List, Optional, Union
from src.retrievers.base import BaseRetriever 

class SimpleCosineRetriever(BaseRetriever):
    def __init__(self,
      k:int,
      encoder,
      vector_store,
      ):
        
        super().__init__(k=k)
        self.topk = k  

        self.encoder = encoder
        self.embedding_dim = encoder.dimension()
        self.vector_store = vector_store

    def forward(self, query: Union[str, List[str]], k:Optional[str] = None) -> Prediction:

      embds =  self.encoder.encode(query)
      if len(embds.shape) == 2:
        embds = np.mean(embds, axis = 0)

      topk_results = self.vector_store.query(embds, topk=self.topk)

      return [dotdict({"long_text": result.payload['text']}) for result in topk_results]

    def upsert_batch(self, batch)->None:
      batch['vectors'] = self.encoder.encode(batch['text'])
      self.vector_store.upsert_batch(batch)
