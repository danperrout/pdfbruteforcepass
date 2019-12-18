# Decrypt password-protected PDF in Python.
#
# Requirements:
# pip install PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import datetime
import os
import sys

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(output_file)

def decrypt_with_pass(x, arquivo):
    password = ("{:05d}".format(x))      
    try:
        decrypt_pdf(arquivo, 'decrypted_'+arquivo, password)
        print("Sucesso!")
        print(password+' - OK')
        return True
    except:
        print (password, end="\r")
        return False

if __name__ == '__main__':
    inicio = datetime.now()
    max_pass = 99999
    arquivo = 'file_weak_password.pdf'

    print('>> '+arquivo)

    for x in range(max_pass):
        if(decrypt_with_pass(x, arquivo)):
            break

    final  = datetime.now()                     
    duration = final - inicio

    print('     >> FIM! ')                        
    print('     >> Duração da execução do script: '+str(duration))