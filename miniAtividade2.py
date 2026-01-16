base = input("Digite a largura do terreno: ")
altura = input("Digite a profundidade do terreno: ")

area = int(base) * int(altura)

print(f"O terreno possui {area}m²")
if area > 100:
  print("Terreno grande!")