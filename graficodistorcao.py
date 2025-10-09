import matplotlib.pyplot as plt

# dados a serem usados
x1 = [5,7,8,7,6]
y1 = [99,86,87,88,111]

x2 = [9,5,6,7,8]
y2 = [86,103,87,94,78]
plt.scatter(x1, y1, color='blue', label='conjunto 1')
plt.scatter(x2, y2, color='red', label='conjunto 2')
plt.title("Grafico de Dispersao")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()