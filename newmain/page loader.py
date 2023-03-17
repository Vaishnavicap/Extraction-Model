from rake_nltk import Rake
# MAIN Code
import PyPDF2

# Open the PDF file
with open('paper.pdf', 'rb') as f:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(f)

    # Get the number of pages in the PDF file
    num_pages = len(reader.pages)

    # Loop over each page in the PDF file
    for i in range(num_pages):
        # Get the text on this page
        page = reader.pages[i]
        text = page.extract_text()

        # Write the text to a text file
        with open('output.txt', 'a', encoding="utf-8") as outfile:
            outfile.write(text)

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
        
