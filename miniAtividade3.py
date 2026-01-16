salario = int(input("Digite o salario do funcionário: "))

if salario <= 280:
  salario = salario*1.2
elif salario > 280 and salario <= 700:
  salario = salario*1.15
elif salario > 700 and salario <= 1500:
  salario = salario*1.1
else:
  salario = salario*1.05
  
print(f"O novo salário é de R${salario}")