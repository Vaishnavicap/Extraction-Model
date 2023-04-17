# for i in range(10):
#     with open(f"text{i}.txt","w", encoding="utf-8") as file:
#         file.write(str(i))
from PyPDF2 import PdfReader
import io
import re
# creating a pdf reader object
reader = PdfReader('paper.pdf')

page_number = (len(reader.pages))

for i in range(page_number):
    current_page = reader.pages[i]
    cur_pg= current_page.extract_text()
    ran = str(cur_pg)

    with open("text1.txt","a", encoding="utf-8") as file:
        file.write(cur_pg)

with open("text1.txt", 'r', encoding="utf-8") as f:
    x =str(f.read())

    for i in range(1, 69):
        s1 = f"Q.{i}"
        s2 = f"Q.{i+1}"
        idx1 = x.index(s1)
        idx2 = x.index(s2) + 1
        res = ""

        for idx in range(idx1 + len(s1) + 1, idx2):
            res = res + x[idx]
        print(res)