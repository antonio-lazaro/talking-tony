from .simple import SimpleTokenizer
from typing import List


_TOKENIZERS = {
    "default": SimpleTokenizer,
    "simple": SimpleTokenizer
}


class Tokenizer:
    def __init__(self, tokenizer_name: str = "default"):
        self.tokenizer = _TOKENIZERS[tokenizer_name]()


    def tokenize(self, phrase: str) -> List[str]:
        """Tokenize phrase"""
        tokens = self.tokenizer.tokenize(phrase)
        return tokens
