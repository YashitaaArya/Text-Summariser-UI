# Text Summariser UI

This repository contains a Graphical User Interface (GUI) for text summarization. The GUI allows users to input text or URLs and generates summaries using natural language processing (NLP) techniques.
<br>
The text_summarizer() function is a text summarization function that uses spaCy, a natural language processing library in Python. It works by tokenizing the input text, removing stop words, and building a word frequency dictionary. It then calculates the sentence scores based on the sum of word frequencies in each sentence and selects the top N sentences with the highest scores. Finally, it returns the summarized text as a string.

The function first loads the spaCy model for English language using spacy.load('en_core_web_sm'). It then imports stop words from spacy.lang.en.stop_words and punctuation marks from the string module.

The function takes in a single argument raw_docx, which is the raw text to be summarized. The text is first tokenized using spaCy nlp() function, and the stop words are converted to a list. A word frequency dictionary is then built by iterating through each token and checking if it is not a stop word. If a token is not a stop word, it is added to the word frequency dictionary. If it is already present in the dictionary, its frequency is incremented by 1.

The maximum frequency of any word in the dictionary is then calculated, and each word frequency is normalized by dividing it by the maximum frequency. This step helps to reduce the bias towards longer sentences.

The input text is then split into sentences using spaCy's docx.sents. The sentence scores are calculated by iterating through each sentence and adding the normalized frequency of each word in the sentence. The scores are then added to a dictionary where the key is the sentence, and the value is the sentence score.

The function then selects the top 7 sentences with the highest scores using the nlargest() function from the heapq module. Finally, the function returns the summarized text as a string by joining the selected sentences.

## Features

- Summarize text input by the user.
- Summarize text extracted from a URL.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YashitaaArya/Text-Summariser-UI.git
   ```
2. 
