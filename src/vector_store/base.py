from abc import ABC, abstractmethod

class IVectorStore(ABC):

  @abstractmethod
  def __init__(self,
    STORAGE_PATH: str,
    INDEX_NAME: str,
    EMBEDDING_DIM: int,
  ):
    pass

  @abstractmethod
  def upsert_batch(self, batch):
    pass

  @abstractmethod
  def query(self, embd_vector, topk=3):
    pass

  @abstractmethod
  def __del__(self):
    pass