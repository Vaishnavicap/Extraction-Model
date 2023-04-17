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





# # Define the question paper as a string
# question_paper = "Q1. What is the capital of France?\nA. Paris\nB. London\nC. Rome\nD. Madrid\n\nQ2. What is the highest mountain in the world?\nA. Mount Everest\nB. Mount Kilimanjaro\nC. Mount Fuji\nD. Mount Rushmore\n\nQ3. Who invented the telephone?\nA. Alexander Graham Bell\nB. Thomas Edison\nC. Nikola Tesla\nD. Benjamin Franklin\n"

# # Define the question number and answer you are looking for
# question_number = "Q1"
# answer = "Paris"

# # Find the index of the question number in the question paper
# start_index = question_paper.find(question_number)

# # Find the index of the next question number in the question paper
# end_index = question_paper.find("Q", start_index + 1)

# # If this is the last question in the paper, set the end index to the end of the string
# if end_index == -1:
#     end_index = len(question_paper)

# # Extract the question and answer from the substring
# substring = question_paper[start_index:end_index]
# question = substring.split("\n")[0]
# answer_options = substring.split("\n")[1:-1]

# # Find the index of the correct answer in the answer options
# correct_index = answer_options.index(answer)

# # Extract the letter of the correct answer
# correct_letter = chr(correct_index + ord("A"))

# # Print the question and the correct answer
# print(question)
# print(correct_letter)








# with open("text1.txt", 'w', encoding="utf-8") as file:
#     print()
#     lines = file.readlines()
    
#     # Initialize a variable to keep track of the current question number
#     current_question_number = "Q"
    
#     # Loop through each line in the file
#     for line in lines:
#         # Check if the line starts with a number followed by a dot, which indicates a new question
#         if line.strip().startswith(str(current_question_number + 1) + '.'):
#             # Increment the current question number
#             current_question_number += 1
#             # Print the question number and the question text
#             print(f'{current_question_number}. {line.strip()}')



# Open the text file containing the questions
# with open('text1.txt', 'r', encoding='utf-8') as f:
#     # Read the lines from the file
#     lines = f.readlines()
    
#     # Initialize a variable to keep track of the current question number
#     current_question_number = 0
    
#     # Loop through each line in the file
#     for line in lines:
#         # Check if the line starts with a number followed by a dot, which indicates a new question
#         if line.strip().startswith(str(current_question_number + 1) + '.'):
#             # Increment the current question number
#             current_question_number += 1
#             # Print the question number and the question text
#             print(f'{current_question_number}. {line.strip()}')



# with open('text1.txt', 'r+', encoding='utf-8') as f:
#     # Read the lines from the file
    
#     lines = f.readlines()
    
#     # Initialize a variable to keep track of the current question number
#     current_question_number = 0
    
#     # Loop through each line in the file
#     for line in lines:
#         # Check if the line starts with a number followed by a dot, which indicates a new question
#         if(line.strip().startswith(str(current_question_number + 1) + '.') and line.strip().endswith("(")):
#             # Increment the current question number
#             current_question_number += 1
#             # Print the question number and the question text
#             print(f'{current_question_number}. {line.strip()}')
            
