par = 0
impar = 0

for x in range(5):
    numero = int(input("Me diga um numero: "))
    if(numero %2 == 0):
        par +=1
    else:
        impar +=1
        
print(f"Quantidade de Numeros pares: {par}")
print(f"Quantidade de Numeros impares: {impar}")