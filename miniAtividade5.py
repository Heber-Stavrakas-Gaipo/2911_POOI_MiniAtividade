vetor = []
i = 0

while i < 100:
  vetor.append(int(input(f"Digite o número na posição {i}: ")))
  opcao = input("Deseja digitar mais um número? SIM/NÃO: ")
  if(opcao.lower() == "não"):
    break;
  i += 1
  
somaPositivos = 0
somaNegativos = 0
contaPositivos = 0
contaNegativos = 0
for num in vetor:
  if num > 0:
    somaPositivos += num
    contaPositivos+= 1
  elif num < 0:
    somaNegativos += num
    contaNegativos+=1
    
mediaPositivos = somaPositivos/contaPositivos
mediaNegativos = somaNegativos/contaNegativos

print(f"Soma dos números positivos: {somaPositivos}\nSoma dos números negativos: {somaNegativos}\nMédia dos números positivos: {mediaPositivos}\nMédia dos números negativos: {mediaNegativos}\nDiferença entre a quantidade de positivos ({contaPositivos}) e negativos ({contaNegativos}): {contaPositivos-contaNegativos}")
  