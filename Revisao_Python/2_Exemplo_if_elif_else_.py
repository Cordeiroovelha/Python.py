# ------------------------------------------
# Aula: Estruturas de Decisão (if, elif, else)
# ------------------------------------------

# Entrada de dados (input)
nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

# Estruturas de decisão
if nota >= 6:
    print(f"{nome}, você foi APROVADO! ")
    print("Excelente desempenho, continue assim!")
elif nota >= 4:
    print(f"{nome}, você está em RECUPERAÇÃO! ")
    print("Ainda dá tempo de melhorar, não desanime!")
else:
    print(f"{nome}, você foi REPROVADO. ")
    print("Procure revisar os conteúdos e tentar novamente.")

# Mensagem final
print("\nFim do programa. Boa sorte nos estudos!")
