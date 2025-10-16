# Crie um programa que imprima uma contagem regressiva iniciando em 10. 
# E quando chegar em zero imprima “Vai!!!”

print( 'Contagem regressiva')
i = 10
while i >= 0:
    if(i==0):
        print( 'Vai!!!')
    else:
        print( ' = ', i)
    i = i - 1
