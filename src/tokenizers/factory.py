from src.tokenizers.CharacterTokenizer import CharacterTokenizer
from enum import Enum

class TokenizerType(Enum):
  Character = 'Character'

def tokenizer_factory(tokenizerType):
  if tokenizerType == TokenizerType.Character:
    return CharacterTokenizer()
  else:
    raise ValueError(f"TokenizerType {tokenizerType} not recognized")