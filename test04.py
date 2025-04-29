nota=[""]*5
soma =0
contador=0
for i in range(len(nota)):
    nota[i]=float(input("digite a nota:"))
for j in range(5):
    soma=soma+nota[j]
media=soma/5
for x in range(5):
    if nota[i]>media:
        contador=contador+1
    print(f"{contador}notas maiores que a {media}")
