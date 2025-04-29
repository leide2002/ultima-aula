nomes=["jimin","jungkook","nanjoon","taeyhung,yongi"]
pesquisa= input("digite o nome para pesquisar:")
for x in range (len(nomes)):
    if pesquisa==nomes[x]:
        msg=f"achei o {pesquisa}na posição{x}"
else:
    msg="nome não encontrado"
    print(msg)