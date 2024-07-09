from abc import ABC, abstractmethod
from src.dataloaders import pubmed

class IDataLoader(ABC):
  @abstractmethod
  def __init__(self,
    data_dir,
    tokenizer,
    batch_size,
    max_tokens, 
    test
  ):
    pass

  @abstractmethod
  def __len__(self):
    pass

  @abstractmethod
  def __iter__(self):
    pass


