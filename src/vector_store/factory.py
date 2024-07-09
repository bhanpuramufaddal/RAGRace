from src.vector_store.qdrant import QdrantVectorStore
from enum import Enum

class VectorStoreType(Enum):
  QDRANT = QdrantVectorStore

def vector_store_factory(
  storage_path: str,
  index_name: str,
  embedding_dim: int,
  store_type: VectorStoreType,
):
  return store_type.value(
    storage_path,
    index_name,
    embedding_dim,
  )

