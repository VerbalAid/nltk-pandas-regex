# 1. Lexical Diversity Function
def lexical_diversity(text):
    return len(set(text)) / len(text)

# 2. Lexical Diversity of 9 nltk texts
from nltk.book import *

books = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
diversities = {book: lexical_diversity(book) for book in books}
richest_text = max(diversities, key=diversities.get)

print("Lexical Diversity:")
for book, diversity in diversities.items():
    print(f"Text {books.index(book)+1}: {diversity:.2f}")
    
print(f"\nText with the greatest lexical diversity: {richest_text}")

# 3. 30 most frequently occuring words of a text, excluding stop words
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def most_frequent_words(text, num=30):
    stop_words = set(stopwords.words('english'))
    lower_words = [word.lower() for word in text if word.isalpha()]
    words = [word for word in lower_words if word not in stop_words]
    freq_dist = FreqDist(words)
    return freq_dist.most_common(num)

# 4. 30 most frequently occuring words in nltk.book package.

for i, book in enumerate(books, start=1):
    most_common = most_frequent_words(book)
    print(f"\n30 most frequently occurring words in text{i}:")
    for word, frequency in most_common:
        print(f"{word}: {frequency}")

# 5 Count in Romance section of the Brown Corpus a selection of wh words, such as what, when, where,who, and why.

from nltk.corpus import brown
romance_words = brown.words(categories='romance')
wh_words = [word.lower() for word in romance_words if word.lower() in {'what', 'when', 'where', 'who', 'why'}]
count = len(wh_words)

print(f"\nCount of wh- words in the Romance section of the Brown Corpus: {count}")

# 6. Lemminsing and tokensing the Gutenberg text into two seperate files and comparing them

from nltk.corpus import gutenberg
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from urllib.request import urlopen

url = "https://www.gutenberg.org/files/2554/2554-0.txt"
raw_text = urlopen(url).read().decode('utf-8')

wnl = WordNetLemmatizer()
tokens = word_tokenize(raw_text)
lemmas = [wnl.lemmatize(token.lower()) for token in tokens if token.isalpha()] 

with open('tokens.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(tokens))

with open('lemmas.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lemmas))

# The count of unique tokens and lemmas

unique_tokens = set(tokens)
unique_lemmas = set(lemmas)

print(f"Unique tokens: {len(unique_tokens)}")
print(f"Unique lemmas: {len(unique_lemmas)}")
print(f"Difference in vocabulary size: {len(unique_tokens) - len(unique_lemmas)}")

# 7. A function that computes what percentage of the text is taken up by a specific word.

def word_percentage(word, text):
    word = word.lower()
    text = [word.lower() for word in text if word.isalpha()]
    count = text.count(word)
    percentage = (count / len(text)) * 100 if len(text) > 0 else 0
    return percentage

# 8. Download two news articles from different genres. Clean the html tags using BeautifulSoup, 
# and tokenize the files. Remove stopwords. Use the function defined in the previous exercise to obtain
# differences in percentage use of a certain word depending of the genre.

import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import string

url_tech = "https://www.bbc.com/news/articles/c867vyn2evlo"
url_politics = "https://www.bbc.com/news/articles/cvg4337rxy1o"

response_tech = requests.get(url_tech)
response_politics = requests.get(url_politics)

# Save raw HTML files 
with open('tech_article.html', 'w', encoding='utf-8') as f:
    f.write(response_tech.text)
with open('politics_article.html', 'w', encoding='utf-8') as f:
    f.write(response_politics.text)

# Step 2: Clean HTML
def clean_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text(separator=' ', strip=True)

tech_text = clean_html(response_tech.text)
politics_text = clean_html(response_politics.text)

# Save cleaned text 
with open('tech_cleaned.txt', 'w', encoding='utf-8') as f:
    f.write(tech_text)
with open('politics_cleaned.txt', 'w', encoding='utf-8') as f:
    f.write(politics_text)

# Step 3: Tokenize and remove stopwords and punctuation
def clean_tokens(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    return [word for word in tokens if word not in stop_words and word.isalpha()]

tech_tokens = clean_tokens(tech_text)
politics_tokens = clean_tokens(politics_text)

# Step 4: Compare word usage 
target_word = "government"  
percent_tech = word_percentage(target_word, tech_tokens)
percent_politics = word_percentage(target_word, politics_tokens)

print(f"Percentage of '{target_word}' in tech: {percent_tech:.2f}%")
print(f"Percentage of '{target_word}' in politics: {percent_politics:.2f}%")
print(f"Difference: {(percent_tech - percent_politics):.2f}%")


