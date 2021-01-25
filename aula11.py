#Aula 11 - Tratamento de erros e exceções 

import time 

def abre_arquivo():
    try:
        arq = open("arquivo.txt")
        return arq
    except Exception as err: 
        print("Some error: ", err)
        return None


while not abre_arquivo():
    print("Trying to open the file!")
    time.sleep(5)

print("Consegui abrir o arquivo")