from src.vector_store.base import IVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, Batch


class QdrantVectorStore(IVectorStore):
  def __init__(self,
    storage_path,
    index_name,
    embedding_dim,
  ):
    self.client = QdrantClient(path=storage_path)
    self.index_name = index_name

    self.client.create_collection(
      collection_name=index_name,
      vectors_config=VectorParams(
        size=embedding_dim,
        distance=Distance.DOT),
      )
    
  def upsert_batch(self, batch):
    self.client.upsert(
      collection_name=self.index_name,
      points=Batch(
        ids=batch['idx'],
        vectors=batch['vectors'].tolist(),
        payloads=batch['metadata'],
      )
    )

  def query(self, embd_vector, topk=3):
    topk = self.client.search(
      collection_name=self.index_name,
      query_vector=embd_vector,
      limit=topk,
      with_vectors=False,
    )
    topk = [result.payload for result in topk]
    return topk

  def __del__(self):
    self.client.delete_collection(
      collection_name=self.index_name,
      )
    self.client.close()