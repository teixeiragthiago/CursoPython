class Cliente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def exibirDados(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Idade:", self.idade)