
from .most_times import MostTimes
from ..tokenizers import Tokenizer

_MODELS = {
    "base": MostTimes,
    "most-times": MostTimes
}

class TalkingTony:
    """Root model"""

    def __init__(self, model_name: str, tokenizer: Tokenizer = Tokenizer()):
        self.model = _MODELS[model_name](tokenizer)


    def train(self, df):
        """
        Train the model
        
        Parameters
        ----------
        df : DataFrame
            Pandas DataFrame with one column for the questions and other for
            their corresponding answers.
        """
        self.model.train(df)


    def answer(self, question: str) -> str:
        """
        Get answer to the given question
        
        Parameters
        ----------
        question : str
            Question to ask the bot.
            
        Returns
        -------
        answer : str
            The answer to the given question
        """
        r = self.model.answer(question)
        return r
        
