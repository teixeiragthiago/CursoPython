import sys

"""
    Aula 08 - Passagem de argumentos com linhas de comando
"""

argumentos = sys.argv # arg1 método // arg2 - n1 // arg3 - n2

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if(argumentos[1]) == "soma":
    ans = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    ans = sub(float(argumentos[2]), float(argumentos[3]))

print(ans)