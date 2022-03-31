"""
Author:
Carlo Lipizzi
Info at clipizzi@stevens.edu


This script takes a clean non n-grammed text and calculate the sentiment "embedded" in it.
It uses the library "vader".
The output is a set of 3 values:
    negative
    neutral
    positive.

"""

# importing the required libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def txt_clean(word_list, min_len, stopwords_list):
    """
    Performs a basic cleaning to a list of words.

    :param word_list: list of words
    :type: list
    :param min_len: minimum length of a word to be acceptable
    :type: integer
    :param stopwords_list: list of stopwords
    :type: list
    :return: clean_words list of clean words
    :type: lists

    """
    clean_words = []
    for line in word_list:
        parts = line.strip().split()
        for word in parts:
            word_l = word.lower().strip()
            if word_l.isalpha():
                if len(word_l) > min_len:
                    if word_l not in stopwords_list:
                        clean_words.append(word_l)
                    else:
                        continue

    return clean_words

'''
----------- Main
'''

# Parameters definition
text_file = 'ISIS_Finance_Nov15.txt'
stp_file = 'stopwords_en.txt'
word_min_len = 2

# reading the input file
input_file = open(text_file, 'r', encoding='utf8')

# initializing list of input words
in_file = []

# populating the list of words from the text file
for word in input_file:
    if word != '\n':
        in_file.append(word)

# opening the stopword file
stopwords_file = open(stp_file,'r', encoding='utf8')

# initializing list of stopwords
stopwords = []

# populating the list of stopwords
for word in stopwords_file:
    stopwords.append(word.strip())

# cleaning the input text
clean_text = txt_clean(in_file, word_min_len, stopwords)

# calculating the sentiment using vader library
analyzer = SentimentIntensityAnalyzer()

# vader needs strings as input. Transforming the list into string
clean_text_str = ' '.join(clean_text)
vad_sentiment = analyzer.polarity_scores(clean_text_str)

pos = vad_sentiment ['pos']
neg = vad_sentiment ['neg']
neu = vad_sentiment ['neu']

print ('\nThe following is the distribution of the sentiment for the file -', text_file)
print ('\n--- It is positive for', '{:.1%}'.format(pos))
print ('\n--- It is negative for', '{:.1%}'.format(neg))
print ('\n--- It is neutral for', '{:.1%}'.format(neu), '\n')

