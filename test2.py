# importing required modules
from PyPDF2 import PdfReader
import io
# creating a pdf reader object
reader = PdfReader('paper.pdf')

# printing number of pages in pdf file
page_number = (len(reader.pages))
print( page_number)

# getting a specific page from the pdf file
# page = reader.pages[10]
# j = 1
for i in range(page_number):
    current_page = reader.pages[i]
    print("===================")
    print("Content on page:" + str(i + 1)) #page num denote
    print("===================")
    # print(current_page.extract_text())
    x_xx= current_page.extract_text()
    ran = str(x_xx)
    # print("Alt")
    print(ran)
    with open("text1.txt","a", encoding="utf-8") as file:
        file.write(x_xx)
    

# print(ran)
# extracting text from page
# text = page.extract_text()
# print(text)
# with open("text1.txt","w") as file:
#     file.write(text)



