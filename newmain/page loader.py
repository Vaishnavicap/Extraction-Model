from rake_nltk import Rake
# Open the text file
# MAIN Code
r = Rake()
arr = []
with open('output.txt', 'r', encoding='utf-8') as f:
    paragraph = ''

  
    # Loop through each line in the file
    for line in f:
        if line.startswith('Q.'):
            # If so, reset the paragraph and start building a new one
            paragraph = line
        # If the paragraph has already started, add the line to it
        elif paragraph and not line.startswith('(A)'):
            paragraph += line
        # If the line starts with 'A', the paragraph is complete, so print it
       
        elif line.startswith('(A)'):
            r.extract_keywords_from_text(paragraph)
            # print(r.get_ranked_phrases())
            # print("************************")
            with open('keywords.txt', 'a', encoding='utf-8') as file:
                file.write(f"{r.get_ranked_phrases()} \n************************\n")
                

            # print(paragraph)
            # arr.append(paragraph)
            # print("************************")
            # Reset the paragraph
            paragraph = ''
        
