# Aula 05 - Laços de Repetição. While e For

nomes = ["Thiago", "Marcelo", "Rafaela", "Júlia"]

#sem usar índice
# for nome in nomes:
#     print(nomes)

# usando índice
# for i in range(len(nomes)):
#     print(nomes[i])

# i = 0
# while i < len(nomes):
#     print(nomes[i])
#     i +=1 # Python não tem i++


"""
    Exercício: Faça um programa que leia a qtd de pessoas que serão convidadas para uma festa.
    
    Após isso, o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
    Após issi irá imprimir todos os nomes da lista
"""

qtdConvidados = input("Digite a quantidade de convidados: ")

convidados = []

for i in range(int(qtdConvidados)):
    convidado = input("Digite o nome do convidado: ")
    convidados.append((convidado))

print("\n Os convidados da festa são: ")
for nome in convidados:
    print(nome)
