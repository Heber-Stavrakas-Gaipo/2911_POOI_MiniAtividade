valor = int(input("Digite um valor: "))
fibonacci = []
i = 0

while i < valor:
  if i == 0:
    fibonacci.append(0)
  elif i == 1:
    fibonacci.append(1)
  else:
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
  i += 1

print(f"A Sequência de Fibonacci para o critério de parada {valor} é: {fibonacci}")