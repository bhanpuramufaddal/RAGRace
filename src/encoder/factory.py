from enum import Enum
from src.encoder.sentence_transformer_encoder import SentenceTransformerEncoder

class EncoderType(Enum):
    """
    An enumeration of the different types of encoders.
    """
    SENTENCE_TRANSFORMER = "sentence_transformer"

def encoder_factory(encoder_type: EncoderType, **kwargs):
    """
    Creates an encoder of the specified type.

    Parameters:
    encoder_type (EncoderType): The type of encoder to create.
    **kwargs: The keyword arguments to pass to the encoder.

    Returns:
    IEncoder: The encoder.
    """
    if encoder_type == EncoderType.SENTENCE_TRANSFORMER:
        return SentenceTransformerEncoder(**kwargs)
    else:
        raise ValueError(f"Unsupported encoder type: {encoder_type}")
