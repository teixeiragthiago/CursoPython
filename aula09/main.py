from conta import  Conta
from cliente import Cliente

# from veiculo import Veiculo
# from carro import Carro
#
# veic1 = Veiculo("Preto", 4, "Peugeot", 10)
#
# veic1.exibirdados()
#
# print("\n\n")
#
# carr1 = Carro("Branco", "FIAT", 10)
#
# carr1.exibirdados()
#
# carr1.abastecer(60)

"""
    Crie um software de gerenciamento bancário
    Esse soft poderá ser capaz de criar clientes e contas
    Cada cliente possui nome, cpf e idade
    Cada conta possui um cliente, saldo, limite, métodos: sacar, depositar e consultar saldo
"""

# cliente1 = Cliente("Thiago", 46065191850, 23)
# cliente1.exibirDados()

conta1 = Conta("Thiago", 6000, 10000)

conta1.depositar(0)

