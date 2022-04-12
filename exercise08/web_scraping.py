# import the libraries
import bs4 as bs
import requests

# getting the content
body = requests.get('https://www.nytimes.com')
soup = bs.BeautifulSoup(body.content,'html.parser')

# printing the title
print ('\n', soup.title.string, '\n')

# Extract the plain text content from paragraphs
for paragraph in soup.find_all('p'):
    print(paragraph.text, '\n')
