import openpyxl
from docxtpl import DocxTemplate
import datetime

# Excel
caminho = 'student_data.xlsx' # informando o arquivo que vai ser utilizado
pasta_trabalho = openpyxl.load_workbook(caminho) # abrindo o arquivo excel caminho em python
sheet = pasta_trabalho.active # informando a janela do excel que vai ser usada

lista_valores = list(sheet.values)

# World

doc = DocxTemplate('certificate.docx')

# o [1:] no for é para ignorar a primeira linha do arquivo excel que no caso é o titulo
for x in lista_valores[1:]:
    doc.render({
        'nome':x[0],
        'curso':x[1],
        'data':x[2].strftime('%d/%m/%Y'),
        'instrutor':x[3]
    })
    doc_nome = f'Certificado {x[0]}.docx'
    doc.save(doc_nome)