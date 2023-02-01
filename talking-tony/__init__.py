import os
import pandas as pd
from .models import _MODELS, TalkingTony
from .tokenizers import _TOKENIZERS, Tokenizer


_LANGUAGES = ["en"]


def load_model(name: str, ln: str = "en", tokenizer: str = "default") -> TalkingTony:
    """
    Load a TalkingTony model

    Parameters
    ----------
    name : str
        one of the names of the different models available.
    ln : str
        one of the languages short-name of the different languages available.
    tokenizer : str
        one of the tokenizers of the different available.

    Returns
    -------
    model : TalkingTony
        The TalkingTony model instance
    """
    if name not in _MODELS:
        raise RuntimeError(f"Model {name} not found; available models = {list(_MODELS.keys())}")

    if ln not in _LANGUAGES:
        raise RuntimeError(f"Language {ln} not found; available languages = {_LANGUAGES}")

    if tokenizer not in _TOKENIZERS:
        raise RuntimeError(f"Tokenizer {tokenizer} not found; available tokenizers = {list(_TOKENIZERS.keys())}")
    
    model = TalkingTony(name, tokenizer = Tokenizer(tokenizer))
    base_path = os.path.dirname(os.path.dirname(__file__))
    train_df = pd.read_csv(f"{base_path}/data/{ln}.csv", sep=";")
    model.train(train_df)

    return model
