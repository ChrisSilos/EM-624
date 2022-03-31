# Sample of text processing

# import nltk libraries
import nltk

# input the text
text = 'Feisty and frequently sarcastic Sanders could barely contain his disgust with Clinton ties with Wall Street a ripe target among liberals in New York City and in economically depressed upstate regions After Clinton said she had stood up to bankers and called them out on their shaky financial practices before the recession Sanders delivered his retort with the flair of a veteran Broadway actor'

# extract and print the tokens from the text
tokens = nltk.word_tokenize(text)
print ('\n------list of tokens in the text:')
print (tokens)

# calculate and print the most frequent words/tokens
freqdist = nltk.FreqDist(tokens).most_common(2)
print ('\n------the 2 most frequent words are:')
print (freqdist)

# tag and print the words for part of speech
tagged = nltk.pos_tag(tokens)
print ('\n------the following are the words tagged for POS:')
print (tagged)

# calculate and print bigrams
bigrammed = list(nltk.bigrams(tokens))
print ('\n------the following are the bigrams extracted from the text:')
print (bigrammed)

# working with stopwords in NLTK
stop = set(nltk.corpus.stopwords.words('english'))
print ('\n------words in the text that are not stopwords:')
print ([single_word for single_word in text.lower().split() if single_word not in stop])

# calculate and print list of gutemberg library titles
gutenberg_titles = nltk.corpus.gutenberg.fileids()
print ('\nlist of titles in Gutenberg library:')
print (gutenberg_titles)


# removing stopwords without NLTK - reading an input and a stopwords text files
# reading the input file and remove some special characters
NewString = open('DemocraticDebate_NYT.txt', encoding='utf8').read().replace('\n','').replace('\t','')

# removing non alphabetical characters
NewStringAlpha = ''.join([word for word in NewString if not word.isdigit()])
# opening the stopword file and reading it into a list
Stopword_List = open("stopwords_en.txt", encoding='utf8').read().splitlines()
# filtering out stop words
Filtered_list = [word for word in NewStringAlpha.lower().split() if word not in Stopword_List]
Filtered_string = ' '.join(Filtered_list)
# printing results
print ('\n------words in the text that are not stopwords (as a list):')
print (Filtered_list)

print ('\n------words in the text that are not stopwords (as a string):')
print (Filtered_string)
