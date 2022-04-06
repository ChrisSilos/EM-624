# Author -- Chris Silos
# EM 624

# Exercise 07

# This is a program that cleans and analyzes text discussing the pros and cons of privatized prisons

# The program outputs the following information for each text file
# 1. Sentiment analysis (using Vader library)
# 2. Word cloud displaying the most frequently used words in each text 

# Import libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import nltk
nltk.download('punkt')

# Open pros, cons, and stopwords file
pros_file = open('Pros.txt','r')
cons_file = open('Cons.txt','r')
stopwords_file = open('stopwords_en-2.txt','r')

# Initialize lists
stopwords = []
pros_words = []
cons_words = []

# Populate list of stopwords
for word in stopwords_file:
    stopwords.append(word.strip())

# Update the stopword list 
stopwords.extend(['pro','con','public','private','prison','prisons','zealand'])

# Create list of words from the pros input file
for pros_file, pros_list in [(pros_file, pros_words)]:
    for line in pros_file:
        parts = line.strip().split()
        for word in parts:
            pros_list.append(word.lower())

# Create list of words from the cons input file
for cons_file, cons_list in [(cons_file, cons_words)]:
    for line in cons_file:
        parts = line.strip().split()
        for word in parts:
            cons_list.append(word.lower())

# Tokenize each text
pros_tokens = nltk.word_tokenize(' '.join(pros_list))
cons_tokens = nltk.word_tokenize(' '.join(cons_list))  

# Create list of cleaned pros words
cleaned_pros = []
for token in pros_tokens:
    # Only append tokens that are NOT stopwords, are alphanumeric, and are greater than 3 characters
    if (token.lower() not in stopwords) and (token.isalnum()) and (len(token)>3):
        cleaned_pros.append(token.lower())

# Create list of cleaned cons words
cleaned_cons = []
for token in cons_tokens:
    # Only append tokens that are NOT stopwords, are alphanumeric, and are greater than 3 characters
    if (token.lower() not in stopwords) and (token.isalnum()) and (len(token)>3):
        cleaned_cons.append(token.lower())

# Extract bigrams for each text
pros_bigrams = list(nltk.bigrams(cleaned_pros))
cons_bigrams = list(nltk.bigrams(cleaned_cons))

# Calculate the sentiment using vader library
pros_analyzer = SentimentIntensityAnalyzer()

# vader needs strings as input. Transforming the list into string
pros_clean_text_str = ' '.join(cleaned_pros)
vad_sentiment = pros_analyzer.polarity_scores(pros_clean_text_str)

pos = vad_sentiment ['pos'] * 100
neg = vad_sentiment ['neg'] * 100
neu = vad_sentiment ['neu'] * 100

print ('\nThe following is the distribution of the sentiment for the PROS file -')
print (f'\n--- It is positive for {pos:.1f}%')
print (f'\n--- It is negative for {neg:.1f}%')
print (f'\n--- It is neutral for {neu:.1f}%', '\n')

# Calculate the sentiment using vader library
cons_analyzer = SentimentIntensityAnalyzer()

# vader needs strings as input. Transforming the list into string
cons_clean_text_str = ' '.join(cleaned_cons)
vad_sentiment = pros_analyzer.polarity_scores(cons_clean_text_str)

pos = vad_sentiment ['pos'] * 100
neg = vad_sentiment ['neg'] * 100
neu = vad_sentiment ['neu'] * 100

print ('\nThe following is the distribution of the sentiment for the CONS file -')
print (f'\n--- It is positive for {pos:.1f}%')
print (f'\n--- It is negative for {neg:.1f}%')
print (f'\n--- It is neutral for {neu:.1f}%', '\n')

# Define the wordcloud parameters for pros file
pros_wc = WordCloud(background_color = 'white', max_words=2000)

# Generate word cloud for pros file
pros_wc.generate(' '.join(cleaned_pros))

# storing to file
pros_wc.to_file('pros.png')

# Show the cloud
plt.imshow(pros_wc)
plt.axis('off')
plt.show()

# Define the wordcloud parameters for cons file
cons_wc = WordCloud(background_color = 'white', max_words=2000)

# Generate word cloud for cons file
cons_wc.generate(' '.join(cleaned_cons))

# storing to file
cons_wc.to_file('cons.png')

# showing the cloud
plt.imshow(cons_wc)
plt.axis('off')
plt.show()