lista = []
i = 0

def contaPessoasAcimaMedia(lista):
  somaDasIdades = 0
  counter = 0
  for idade in lista:
    somaDasIdades += idade
  quantidade = len(lista)
  media = somaDasIdades/quantidade
  for idade in lista:
    if idade > media:
      counter+=1
  return counter

while i < 10:
  lista.append(int(input(f"Digite a idade da pessoa {i+1}: ")))
  i += 1
    
print(len(lista))
print(f"O número de pessoas com idade acima da média é: {contaPessoasAcimaMedia(lista)}")
