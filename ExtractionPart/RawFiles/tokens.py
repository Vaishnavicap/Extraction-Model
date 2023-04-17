import nltk
from nltk.corpus import stopwords
from textblob import TextBlob


# open and read the text file
with open('output.txt', 'r' , encoding='ISO-8859-1') as file:
    text = file.read()

# tokenize text into individual words
tokens = nltk.word_tokenize(text)
# print(tokens)
# print("*******************")

# remove stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
# print(filtered_tokens)
# print("*******************")

# perform stemming
stemmer = nltk.PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
# print(stemmed_tokens)
# print("*******************")

# perform lemmatization
lemmatizer = nltk.WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
# print(lemmatized_tokens)


blob = TextBlob(text)

# define the list of stop words to remove
stop_words = set(stopwords.words('english'))

# extract the noun phrases from the text
noun_phrases = blob.noun_phrases

# filter out stop words from noun phrases
filtered_noun_phrases = [phrase for phrase in noun_phrases if phrase.lower() not in stop_words]

# extract the keywords from the text
keywords = set()
for word, pos in blob.tags:
    if pos.startswith('NN') and word.lower() not in stop_words:
        keywords.add(word.lower())

# add noun phrases to keywords
keywords.update(filtered_noun_phrases)

print("Keywords:", keywords)



# define the text to process

# split the text into individual words
# words = text.split()

# # remove stop words
# stop_words = set(stopwords.words('english'))
# filtered_words = [word for word in words if word.lower() not in stop_words]

# # join the filtered words back into a text
# filtered_text = ' '.join(filtered_words)

# # perform spelling correction
# blob = TextBlob(filtered_text)
# corrected_text = str(blob.correct())

# # print("Original Text: ", text)
# print("Filtered Text: ", filtered_text)
# print("Corrected Text: ", corrected_text)
