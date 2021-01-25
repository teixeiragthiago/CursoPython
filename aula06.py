# Lista (list) comum
minha_lista = ["Thiago", "Bruna"]

# Tupla (tuple) -> a tupla não é mutável, é uma estr. de dados readonly
# A tupla, se você for substuir algum dado, vc tem que substituir a tupla INTEIRA!
minha_tupla = ("Thiago", "Bruna")

# Dicionário (dictionary) -> basicamente um json
meu_dicionario = { "nome": "Thiago", "idade": 23 }

# Chegar se existe algo dentro de uma estrutura de dados

# if "Thiago" in meu_dicionario:
#     print("OK, beleza!!")
# else:
#     print("Tá aqui não!!")

# busca em dicionário pela chave
# print(meu_dicionario["nome"])

# meu_dicionario["nome"] = "Rafael"
#
# for data in meu_dicionario.values():
#     print(data)

# if "Thiago" in meu_dicionario.values():
#     print("OK, beleza!!")
# else:
#     print("Tá aqui não!!")

"""
Conjunto (set) -> no conjunto não podem existir itens repetidos, não tem chave e valor, só os itens
O conjunto não é readonly, posso add, remov, upd, etc.. 
O conjunto não é ordenado e não tem índice!

Dica: o conjunto é mais rápido para varrer e fazer busca, pq não é ordenado.. 

"""
meu_conjunto = {"Thiago", "José", "Lourdes"}

meu_conjunto.add("Rafael")

if "Thiago" in meu_conjunto:
    print("Foi encontrado dentro do conjunto")

print(meu_conjunto)

# Como inicializar essas coleções vazias

lista = []
tupla = ()
dicionario = dict() # ou dicionario = {}
conjunto = set()
