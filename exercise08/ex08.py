# Author -- Chris Silos
# EM 624

# Exercise 08

# THIS PROGRAM TAKES 2-3 MINUTES TO FULLY RUN
# - The sentiment analysis is intensive, please wait for it to finish running

# This is a program that cleans and analyzes text from 769 different news articles

# The program does the following for each article
# 1. Combines the 'description' and 'content' sections to get an overview of the information
# 2. Cleans the text by removing stopwords, non alphabetic words, and words 3 characters long or shorter
# 3. Determines whether or not the article is related to COVID-19

# Sentiment analysis is performed on the following:
# 1. All the articles
# 2. Only the articles related to COVID-19

# The program produces a word cloud for the following:
# 1. All the articles
# 2. Only the articles related to COVID-19

# Import libraries
import pandas as pd
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read file into dataframe
df = pd.read_csv('News_2021.csv')

# Fill 'N/A' values with empty spaces so they can be joined without causing an error
df['content'] = df['content'].fillna(' ')
df['description'] = df['description'].fillna(' ')

# Create a new column containing the description and content of each article
df['description&content'] = df.apply(lambda row: ' '.join(
    (row['description'], row['content'])), axis=1)


def related_to_covid(string):
    """
    This function checks whether any words in a given string are related to COVID-19

    """
    covid_words = ['covid', 'vaccine', 'coronavirus',
                   'vaccination', 'antibody', 'moderna', 'pfizer', 'johnson']
    related = False
    for word in string.strip().split():
        word = word.lower()
        if word in covid_words:
            related = True
    return(related)


# Create a new column to determine if each file is related to Covid 19
df['Related_to_covid'] = df.apply(
    lambda x: related_to_covid(x['description&content']), axis=1)


def clean_description(string):
    """
    This function cleans a given string by removing stopwords, non-alphabetic characters, and words shorter than 4 characters. 
    It is intended to be used to clean the 'description&content' column in the dataframe.

    """
    stopwords_file = open('stopwords_en.txt', 'r')
    stopwords = []
    # Update the stopword list
    #stopwords.extend(['said', 'say', 'says'])
    for word in stopwords_file:
        stopwords.append(word.strip())
    clean_words = []
    # Only append the word to the clean words list if it is alphabetic, not a stopword, and longer than 3 characters
    for word in string.strip().split():
        word = word.lower()
        if word.isalpha() and word not in stopwords and len(word) > 3:
            clean_words.append(word)
    return(clean_words)


# Create a column to hold the cleaned text
df['Cleaned_c&d'] = df.apply(
    lambda x: clean_description(x['description&content']), axis=1)

# Create a list of all the words in every article
all_words = []
for list in df['Cleaned_c&d']:
    all_words = all_words + list

# Create dataframe to hold only covid articles
covid_df = df[df['Related_to_covid'] == True]
# Create list to hold words from all articles
covid_words = []
for list in covid_df['Cleaned_c&d']:
    covid_words = covid_words + list

# Create dataframe to hold only non-covid articles
non_covid_df = df[df['Related_to_covid'] == False]
# Create list to hold words from non-covid articles
non_covid_words = []
for list in non_covid_df['Cleaned_c&d']:
    non_covid_words = non_covid_words + list

# Calculate the percentage of articles related to COVID-19
num_covid_articles = len(df[df['Related_to_covid'] == True])
num_total_articles = len(df['Related_to_covid'])
pcntg_related_to_covid = num_covid_articles/num_total_articles*100
print(f'\nPercent of articles relate to COVID-19: {pcntg_related_to_covid:.2f}% ({num_covid_articles}/{num_total_articles}) \n')


def calculate_sentiment(word_list):
    """
    This function calculates the sentiment of a given list of words and prints it to the terminal

    """
    # Calculate the sentiment using vader library
    analyzer = SentimentIntensityAnalyzer()

    # vader needs strings as input. Transforming the list into string
    clean_text_str = ' '.join(word_list)
    vad_sentiment = analyzer.polarity_scores(clean_text_str)

    pos = vad_sentiment['pos'] * 100
    neg = vad_sentiment['neg'] * 100
    neu = vad_sentiment['neu'] * 100

    print(f'\n--- It is positive for {pos:.1f}%')
    print(f'\n--- It is negative for {neg:.1f}%')
    print(f'\n--- It is neutral for {neu:.1f}%', '\n')

# Perform sentiment analysis for all the words in all the articles
print('\nThe following is the distribution of the sentiment for all of the articles -')
calculate_sentiment(all_words)

# Perform sentiment analysis for all the words in the non COVID related articles
print('\nThe following is the distribution of the sentiment for non COVID-19 related articles -')
calculate_sentiment(non_covid_words)

# Find the 20 words with the highest frequency
highest_frequency = Counter(all_words).most_common(20)
# Convert counter object to a dictionary
freq_dict = dict(highest_frequency)
print('\n--- Frequency for 20 most common words in all articles ---\n')
print(freq_dict)
# Print results in a bar chart
fig = plt.figure(figsize=(12,6))
plt.bar(x=freq_dict.keys(), height=freq_dict.values())
plt.xticks(rotation=45)
plt.show()

def make_wordcloud(wordlist,title):
    """
    This function creates a word cloud from a given list of words

    """
    # Define the wordcloud parameters for the file
    wc = WordCloud(background_color='white', max_words=2000)

    # Generate word cloud for pros file
    wc.generate(' '.join(wordlist))

    # Show the cloud
    plt.title(title)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

# Create word cloud for all words in all the articles
make_wordcloud(all_words,'Word Cloud for all Articles')

# Create word cloud for all words in non COVID related articles
make_wordcloud(non_covid_words, 'Word Cloud for non COVID-19 Related Articles')
