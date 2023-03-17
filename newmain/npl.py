from rake_nltk import Rake

# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# Create a RAKE object with default settings
r = Rake()

# Define the input string
input_string = "Rapid Automatic Keyword Extraction (RAKE) is a keyword extraction algorithm that is designed to extract important keywords or phrases from a text document."

# Run RAKE on the input string
r.extract_keywords_from_text(input_string)
print(r.get_ranked_phrases())


