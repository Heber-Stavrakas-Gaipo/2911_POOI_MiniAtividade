texto = input("Digite um texto: ")
counter = 0

for letra in texto:
  if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
    counter += 1
    
print(f"O texto '{texto}' possui {counter} vogais")