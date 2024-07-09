from abc import ABC, abstractmethod

class Tokenizer(ABC):

  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  def get_tokens(self, text):
    pass

  @abstractmethod
  def num_tokens(self, text):
    pass

  @abstractmethod
  def split_text(self, text, max_length):
    pass