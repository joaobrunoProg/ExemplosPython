from random import randint

num=int(randint(1, 5))
tentativa=0
p=0

while p!=num:
    p=int(input("Digite um numero:"))
    tentativa+=1
    if p==num:
        print("Parabéns Você Acertou! Placar: %i" %tentativa)
    elif p<num:
        print("chute um valor maior!")
    else:
        print("chute um valor menor!")
print("Fim do Game :)")
