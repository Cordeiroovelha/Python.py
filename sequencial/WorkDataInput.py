#Input of work data

TotalHours = float(input("entre o total de horas trabalhadas: "))
ValueHour = float(input("entre o valor da hora trabalhada: "))
Discount = float(input("entre o valor do desconto: "))

GrossSalary = TotalHours * ValueHour
TotalDiscount = GrossSalary * (Discount / 100)
NetSalary = GrossSalary - TotalDiscount

print(f"o salario bruto é: R$ {GrossSalary:.2f}")
print(f"o valor do desconto é: R$ {TotalDiscount:.2f}")
print(f"o salario liquido é: R$ {NetSalary:.2f}")