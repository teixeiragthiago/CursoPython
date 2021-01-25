# Aula 04 - Strings e Listas

frase = "Oi, eu sou o Goku!"

lista_nomes = ["João", "Maria", "Thiago", "Diego"]

# Imprimir um range de uma lista/string
# print(frase[0:6])

# print(frase)

# Posso intercalar a selecao dos valores, imprimo 1 pulo 1, etc..
#print(lista_nomes[0:4:2])

# Pego o último valor da lista, pois ele começa contando de trás pra frente
# print(lista_nomes[-1])

#add item na lista

lista_nomes.append("Rafael")
lista_nomes.remove("Thiago")

# Passa o índice de onde quer adicionar na lista
lista_nomes.insert(1,"Bruno")



for nome in lista_nomes:
    print(nome)

