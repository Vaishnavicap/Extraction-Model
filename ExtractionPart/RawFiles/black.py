from rake_nltk import Rake
# Open the text file
# RAW Code
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projectdb"
)

# Get a cursor object
mycursor = mydb.cursor()

r = Rake()
arr = []
with open('output.txt', 'r', encoding='utf-8') as f:
    paragraph = ''

    inside_target = False

    # Loop through each line in the file
    for line in f:
        if line.startswith('Q.'):
            inside_target = True
            # If so, reset the paragraph and start building a new one
            paragraph = line
        # If the paragraph has already started, add the line to it
        elif paragraph and not line.startswith('(A)'):
            inside_target = True
            paragraph += line
        # If the line starts with 'A', the paragraph is complete, so print it

        elif line.startswith('(A)'):
            r.extract_keywords_from_text(paragraph)
            # print(r.get_ranked_phrases())
            # print("************************")
            sql = "INSERT INTO question (id, qt) VALUES (%s, %s)"
            val = (line, paragraph)
            mycursor.execute(sql, val)

            '''
            with open('keywords.txt', 'a', encoding='utf-8') as file:
                file.write(f"{r.get_ranked_phrases()} \n************************\n")
                
            with open('Question.txt', 'a', encoding='utf-8') as l:
                l.write(f"{paragraph} \n************************\n")'''
            
            # print(paragraph)
            # arr.append(paragraph)
            # print("************************")
            # Reset the paragraph
            paragraph = ''


mydb.commit()
        # elif inside_target and line.strip().endswith('____.'):
        #     # If it does, we've reached the end of the target paragraph
        #     inside_target = False
        #     # Add the line to the paragraph
        #     paragraph += line
        #     # Print the paragraph
        #     print(paragraph)

        #     with open('Question.txt', 'a', encoding='utf-8') as l:
        #         l.write(f"{paragraph} \n************************\n")
        #     # Reset the paragraph variable
        #     paragraph = ''
     