notas = []

for x in range(3):
    nota = float(input("Me diga uma nota: "))
    notas.append(nota)
    
media = sum(notas)/3

if(media >= 7):
    print(f"Aprovado com a média: {media:.1f} parabéns")
else:
    print(f"Reprovado com a média: {media:.1f}")