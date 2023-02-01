import pandas as pd
from collections import Counter
from ..tokenizers import Tokenizer


class MostTimes:
    """Get the question with the most similar words"""

    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
        self.words = {}
        self.answers = {}


    def train(self, df: pd.DataFrame):
        """
        Train the model
        
        Parameters
        ----------
        df : DataFrame
            Pandas DataFrame with one column for the questions and other for
            their corresponding answers.
        """
        for _, row in df.iterrows():
            question, answer = row
            self.answers[question.lower()] = answer
            q_words = self.tokenizer.tokenize(question)
            for word in q_words:
                if word in self.words:
                    self.words[word].add(answer)
                else:
                    self.words[word] = {answer}


    def answer(self, question: str):
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
        if question in self.answers:
            return self.answers[question]

        words = self.tokenizer.tokenize(question)

        answers = []
        for w in words:
            if w in self.words:
                answers.extend(self.words[w])

        if len(answers) == 0:
            return "Mmmm, I don't know."

        c = Counter(answers)
        common_answers = c.most_common()
        r = common_answers[0][0]
        return r
