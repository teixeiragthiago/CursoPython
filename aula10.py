import os

#Aula 10 - Entrada e saída de arquivosß

"""
Se não passar nenhum parâmetro, ele abre o arquivo com permissão somente para leitura
e para abrir texto 'rt'

't' -> open text files
'b'-> open binary files    

append -> append to the end of file
write -> will overwrite any existing content

"""

arq = open("arquivo.txt", "a")

arq.write("Cocô fedido!")
arq.close()


#How to remove files

# if os.path.exists("arquivo.txt"):
#   os.remove("arquivo.txt")
# else:
#   print("The file does not exist") 
