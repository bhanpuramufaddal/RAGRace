from src.retrievers.SimpleCosineRetriever import SimpleCosineRetriever
from enum import Enum

class RetrieverType(Enum):
  SIMPLE_COSINE = SimpleCosineRetriever 

def retriever_factory(
  k: int,
  encoder,
  vector_store,
  retriever_type: RetrieverType,
):
  return retriever_type.value(
    k,
    encoder,
    vector_store,
  )
