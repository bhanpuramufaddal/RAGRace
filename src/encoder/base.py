from abc import ABC, abstractmethod

class IEncoder(ABC):
    """
    The base class for all encoders.
    """
    
    @abstractmethod
    def __init__(self, model_name: str):
        """
        Initializes the encoder.

        Parameters:
        model_name (str): The name of the model to use.
        """
        pass

    @abstractmethod
    def encode(self, text: str) -> list:
        """
        Encodes a given text into a numerical representation.

        Parameters:
        text (str): The text to encode.

        Returns:
        list: The numerical representation of the text.
        """
        pass

    @abstractmethod
    def encode_batch(self, texts: list) -> list:
        """
        Encodes a list of texts into a numerical representation.

        Parameters:
        texts (list): The list of texts to encode.

        Returns:
        list: The numerical representations of the texts.
        """
        pass

    @abstractmethod
    def dimension(self) -> int:
        """
        Gets the dimension of the encoder.

        Returns:
        int: The dimension of the encoder.
        """
        pass