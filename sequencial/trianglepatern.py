# criação de um padrão em forma de triângulo
# trianglepatern.py

print("Triangulo equilatero")
print()
n = 5

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

print()
print("Triangulo invertido")
print()
