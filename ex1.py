continuar=True

while continuar != False:
    nome = str(input("Nome do aluno:"))
    nota1 = float(input("Nota prova 1: "))
    nota2 = float(input("Nota prova 2: "))
    nota3 = float(input("Nota prova 3: "))
    nota4 = float(input("Nota prova 4: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4.0

    if media >= 7:
        print (nome, media, "-aprovado")
    elif (media < 7) and(media >= 4):
        print(nome, media, "-final")
    elif media < 4:
        print(nome, media, "-reprovado")
    mensagem = int(input("deseja continuar?<1>Sim ou <2>Não"))
    if mensagem == 1:
        continuar = True
    else:
        continuar = False
