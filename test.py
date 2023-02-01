# importing required modules
from PyPDF2 import PdfReader
import io
# creating a pdf reader object
reader = PdfReader('paper.pdf')

# printing number of pages in pdf file
page_number = (len(reader.pages))
# print( page_number)

# getting a specific page from the pdf file
# page = reader.pages[10]
for i in range(page_number):
    current_page = reader.pages[i]
    # print("===================")
    # print("Content on page:" + str(i + 1)) #page num denote
    # print("===================")
    # print(current_page.extract_text())
    x_xx= current_page.extract_text()
    ran = str(x_xx)
    # print("Alt")
    # print(ran)
    with open("text1.txt","a", encoding="utf-8") as file:
        file.write(x_xx)
with open("text1.txt", 'r', encoding="utf-8") as file:
    x =str(file.read())
for k in range(67):
    s1 = "Q."+str(k+1)
    print(s1)
    s2 = "Q."+str(k+2)
    print(s2)
    # getting index of substrings
    idx1 = x.index(s1)
    # print(idx1)
    idx2 = x.index(s2)
    res = ''
    # getting elements in between
    for idx in range(idx1 + len(s1) + 1, idx2):
        res = res + x[idx]
    print(res)
    print("=======================================================================================================")





