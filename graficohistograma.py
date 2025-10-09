import matplotlib.pyplot as plt

# dados a serem usados
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y2 = [3, 6, 4, 10, 7, 14, 9, 18, 12, 20]

plt.plot(x, y1, label="conjunto 1", color="blue", marker="o")
plt.plot(x, y2, label="conjunto 2", color="red", marker="s")
plt.title("Grafico de Linhas com 2 conjuntos de dados")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.show()