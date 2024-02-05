distancia = int(input("Me diga a distancia da sua viagem (em km): "))
consumo = int(input("Quantos km por litro ele faz? "))
preco = float(input("Qual o valor da gasolina?"))

valor = (distancia/consumo)*preco

print("O valor total é: ",valor)