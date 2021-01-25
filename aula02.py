"""

Bloco de comentários com Python

nome = "Thiago"
idade = 23
altura = 1.75

# o Input sempre retorna uma string, mesmo que o valor informado seja de outro tipo
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
altura = input("Qual a sua altura? ")

print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)


# Concatenção em duas formas, usando vírcula e +, porém, com +
# ele não add um espaço ao final da string e vc não precisa dar um cast das variáveis

print(nome, "tem", idade, "anos e ", altura, "de altura")

numero1 = 23
numero2 = 30

resultado = numero1 + numero2

#potência: numero1 ** numero2

print(resultado)

"""

nome = input("Informe o seu nome: ")
cpf = input("Informe o seu cpf: ")
endereco = input("Informe o seu endereco: ")
idade = input("Informe a sua idade: ")
altura = input("Informe a sua altura: ")
telefone = input("Informe o seu telefone: ")

print("O seu nome é", nome, "voce tem", idade, "anos e ", altura, "de altura")
print("Você mora ", endereco)
print("O seu CPF é", cpf, "e seu numero de telefone é", telefone)

