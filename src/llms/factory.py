from src.llms.gemini import GeminiLM
from enum import Enum

class LLMTypes(Enum):
    GEMINI = GeminiLM

def llm_factory(llm_type: LLMTypes, model_name: str):
    return llm_type.value(model_name)
