from src.tokenizers.base import Tokenizer

class CharacterTokenizer(Tokenizer):
  def __init__(self):
    super().__init__()

  def get_tokens(self, text):
    return list(text)

  def num_tokens(self, text):
    return len(text)

  def split_text(self, text, max_length):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]