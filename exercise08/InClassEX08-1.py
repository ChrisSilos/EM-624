'''
This script scrapes article titles from a given URL
It uses a library - newspaper - created to extract content from news sources

The "newspaper" library can be installed as "newspaper3k"
'''
import newspaper
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# defining the target source
url = 'http://www.nytimes.com'

# extracting a "newspaper object" to be used for further analysis
# The parameter "memoize_articles" determines if we want to download only new article (value "True") or not
paper = newspaper.build(url, memoize_articles = False, language = 'en', fetch_images = False, number_threads = 2)

print ('number of articles:', paper.size()) # this is to print the number of articles in the URL

# downloading the articles
# The sublibraries "parse" and "nlp" provide language processing features. They are compute-intensive
#   It's an easy way to get language processing, with all the limitations of predefined language analysis solutions
# Please note: there is no control on the words/characters being with latin characters

# defining the maximum number of articles for the search
max_art = 5

headlines = []
# searching for specific keywords in the articles
for article in paper.articles[0:max_art]:
    article.download()
    try:
        article.parse()
        article.nlp()
        # the following "if" triages based on some conditions, to be considered as examples
        if article.title is not None and article.title != 'Aug.' and not article.title.startswith('You must'):
            print(article.title)
            headlines.append(article.title)
    except:
        pass

# first graph - WordCloud
str_words = ' '.join(headlines)
wcloud = WordCloud(background_color = 'white',max_words = 2000)
wcloud.generate(str_words)
plt.imshow(wcloud)
plt.axis('off')
plt.show()
print ('\n--WordCloud generated--\n')
