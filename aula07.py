# Aula 07 - Métodos e funções

"""
    Exercício: Escreva uma função que recebe um objeto de coleção
    e retorna o valor do maior número dessa coleção
"""

valores = [10, 4, 5, 1, 3, 20, 6, 50, 120, 119, 200]

def retornaMaiorValor(collect_values):
    maior = collect_values[0]

    for val in collect_values:
        if val > maior:
            maior = val

    return maior


print(retornaMaiorValor(valores))