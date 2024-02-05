nome = input("Me diga seu nome: ")

peso = int(input("Me diga seu peso: "))
altura = float(input("Me diga sua altura: "))

calculoIMC = peso/(altura*altura)


if calculoIMC < 18.5:
    print(f"{nome} está abaixo do peso")
elif calculoIMC > 18.5 and calculoIMC < 24.9:
    print(f"{nome} está com peso normal")
elif calculoIMC > 25 and calculoIMC < 29.9:
    print(f"{nome} está acima do peso")
elif calculoIMC > 30 and calculoIMC < 39.9:
    print(f"{nome} está acima do peso com obesidade grau 1")
elif calculoIMC > 40:
    print(f"{nome} está acima do peso com obesidade grau 2")
