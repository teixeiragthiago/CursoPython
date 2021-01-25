class Conta:

    def __init__(self, cliente, saldo, limite):
       self.cliente = cliente
       self.saldo = saldo
       self.limite = limite

    def consultar_saldo(self):
        print("Saldo em conta:", self.saldo)

    def depositar(self, valor):
        if self.saldo + valor > self.limite:
            print("Você excedeu seu limite de depósitos!")
        elif valor <= 0:
            print("O valor informado para depósito não é válido!")
        else:
            self.saldo += valor
            print("O Cliente", self.cliente, "realizou deposito de R$:", valor)

    def sacar(self, valor):
        if self.saldo - valor < 0:
            print("Você não possui saldo suficiente para sacar!")
        elif valor <= 0:
            print("O valor informado para saque não é válido!")
        else:
            self.saldo -= valor
            print("O Cliente", self.cliente, "realizou saque de R$:", valor)

    def exibirDados(self):
        print("Cliente:", self.cliente)
        print("Saldo:", self.saldo)
        print("Limite:", self.limite)