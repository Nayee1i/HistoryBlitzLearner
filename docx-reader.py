from docx import Document

num = int(input('Переименуйте подготовленный документ в blitzN.docx и введите N: '))

doc = Document(f'blitz{num}.docx')

terms_arr = []

for table in doc.tables:
    for row in table.rows:
        term = []
        for cell in row.cells:
            term.append(cell.text.strip())
        terms_arr.append(term)

file = open(f'blitz{num}.txt','w',encoding='utf-8')
for term in terms_arr:
    file.write(term[0]+'|'+term[1]+'\n')
file.close()
