import matplotlib.pyplot as plt

# dados a serem usados
grupo_a = [12, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25]
grupo_b = [5, 8, 10, 15, 18, 20, 22, 25, 27, 30]

plt.boxplot([grupo_a, grupo_b])
plt.xticks([1, 2], ['Grupo A', 'Grupo B'])
plt.ylabel("Notas")
plt.title("Grafico de Caixa - De notas de alunos")
plt.show()