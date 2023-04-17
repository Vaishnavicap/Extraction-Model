# from rake_nltk import Rake

# # import nltk
# # nltk.download('stopwords')
# # nltk.download('punkt')
# # Create a RAKE object with default settings
# r = Rake()

# # Define the input string
# input_string = "Rapid Automatic Keyword Extraction (RAKE) is a keyword extraction algorithm that is designed to extract important keywords or phrases from a text document."

# # Run RAKE on the input string
# r.extract_keywords_from_text(input_string)
# print(r.get_ranked_phrases())

import nltk

from textblob import TextBlob
from nltk.corpus import stopwords

# define the text to process
text = "Artificial intelligence (AI) is the simulation of human intelligence processes by computer systems. These processes include learning (the acquisition of information and rules for using the information), reasoning (using rules to reach approximate or definite conclusions) and self-correction."

# create a TextBlob object
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
