import matplotlib.pyplot as plt

# dados a serem usados
notas = [5, 6, 7, 8]
frequencia = [10, 15, 20, 5]

plt.bar(notas, frequencia, color='red')
plt.title("Grafico de Barras - De notas de alunos")
plt.xlabel("Notas")
plt.ylabel("Frequencia Absoluta")
plt.xticks(notas)
plt.show()