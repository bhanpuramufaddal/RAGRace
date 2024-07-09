from dspy import Retrieve, Prediction
from dsp.utils import dotdict
from typing import List, Optional, Union
from src.encoder.base import IEncoder
from src.vector_store.base import IVectorStore

class BaseRetriever(Retrieve):
    def __init__(self,
      k:int,
      encoder:IEncoder,
      vector_store:IVectorStore,
      ):
        super().__init__(k=k)
        pass

    def forward(self, query: Union[str, List[str]],
      k:Optional[str] = None) -> Prediction:
      
      pass

    def upsert_batch(self, batch:dict)->None:
      pass
