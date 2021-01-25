# Aula 03 - Operadores Lógicos

"""
var_verdade = True
var_falso = False

if var_verdade == True:
    print("VAR_VERDADE é Verdadeiro!")

# São usadas as palavras chaves 'and' e 'or' e 'not'

print("Opções: \n 1 - Escreve Thiago \n 2- Escreve João \n 3 - Escreve Maria")

opcao = input("Escolha uma opção: ")

if opcao == str(1):
    print("Thiago")
elif opcao == str(2):
    print("João")
elif opcao == str(3):
    print("Maria")
else:
    print("Opção inválida!")

"""

"""
    Exercício: faça um programa que pgt a idade, peso e a altura de uma pessoa
    e decide se ela está apta a entrar no Exército
    
    Para entrar no exército, é preciso ter mais de 18 anos, pesar mais ou igual a 60kg
    e medir mais ou igual a 1.70 mts
"""

idade = input("Informe a sua idade: ")
peso = input("Informe o seu peso: ")
altura = input("Informe a sua altura: ")

if int(idade) < 18:
    print("Você não está apto para entrar no exército!")
elif float(peso) < 60 and float(altura) > 1.70:
    print("Você não está apto para entrar no exército!")
elif float(altura) < 1.70 and float(peso) > 60:
    print("Você não está apto para entrar no exército!")
else:
    print("Ok! Você está apto para entrar no exército!")
