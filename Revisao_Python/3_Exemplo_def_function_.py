def somar(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2
    
def exibir():
    print("Chamou todas as funções e chegou no FIM.")

a = int(input('Digite o n1 '))
b = int(input('Digite o n2 '))

print('soma de ', a, 'e', b, '= ', somar(a,b))
print('subtracao de ', a, 'e', b, '= ', sub(a,b))
exibir()