import matplotlib.pyplot as plt

# dados a serem usados
notas = [5, 6, 7, 8]
frequencia = [10, 15, 20, 5]

plt.pie(frequencia, labels=notas, autopct='%1.1f%%', colors=['lightcoral', 'lightgreen', 'lightskyblue', 'gold'])
plt.title("Grafico de Setor - De notas de alunos")
plt.show()