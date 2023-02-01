# Talking Tony

The purpose of this repository is to test different algorithms, of increasing complexity, for the development of a bot that answers questions based on a predefined question-answer dataset.

## Problem Statement

The objective of the model to be developed is to find the most appropriate answer to a question, given a [set of questions with their respective answers](data/en.csv).

![Model](.github/model.png)

## Setup

I used Python `3.10.8`, but the codebase is expected to be compatible with Python `3.7`.

To install all the dependencies:

```bash
pip install -r requirements.txt
```

## Data

The data consists of a [CSV file](data/en.csv) with two columns: `question` and `answer`. At first, only English will be used, although more languages are intended to be added in the future.

To test the performance of the model, I have defined a test dataset with variations of the initial dataset questions. The dataset consists of a [CSV file](data/en-var.csv) with two columns: `question` and `variation`.

## Python usage

The model can be used within Python: 

```python
tt = __import__("talking-tony")

model = tt.load_model("base")
answer = model.answer("What's your name?")
print(answer)
```
