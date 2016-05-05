#arquivo copia.py - Leitura e escrita de arquivos binarios (imagem)

logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo-copia.png', 'wr')
logo2.write(data)
logo2.close()