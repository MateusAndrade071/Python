nome = input("Me diga seu nome: ")

peso = int(input("Me diga seu peso: "))
altura = float(input("Me diga sua altura: "))

calculoIMC = peso/(altura*altura)

print(nome,"você tem", round(calculoIMC,2),"de massa corporal")