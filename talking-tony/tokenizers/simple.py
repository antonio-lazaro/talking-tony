from typing import List


CONTRACTIONS = {
    "n't": "not",
    "'re": "are",
    "'ll": "will",
    "'s": "is",
    "'ve": "have",
    "'d": "had",
    " u ": "you",
}


class SimpleTokenizer:
    """A super simple class to tokenize phrases"""

    def tokenize(self, phrase: str) -> List[str]:
        """Tokenize phrase"""
        
        # Replace contractions
        for contraction, replacement in CONTRACTIONS.items():
            phrase = phrase.replace(contraction, " " + replacement)
        
        # Remove marks (TODO: use regex)
        marks = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
        for m in marks:
            phrase = phrase.replace(m, "")
            
        # Remove repetition of last letters (something to work on more)
        last_letter = phrase[-1]
        i = -2
        while phrase[i] == last_letter:
            phrase = phrase[:i] + last_letter        

        # Tokenize phrase
        tokens = [word.lower() for word in phrase.split()]

        return tokens
