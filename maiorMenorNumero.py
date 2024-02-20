num = []
maiorNum = None
menorNum = None

for x in range(5):
    numero = int(input("Me diga um numero: "))
    if (maiorNum is None or numero > maiorNum): # se maiorNum é None(vazio) ou numero é maior que maiorNum
        maiorNum = numero
    if (menorNum is None or numero < menorNum): # se menorNum é None(vazio) ou numero é menor que menorNum
        menorNum = numero
        
    
print(f"Menor Numero: {menorNum}")
print(f"Maior Numero: {maiorNum}")