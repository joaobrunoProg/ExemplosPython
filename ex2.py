num=12
adv=0

while adv!=num:
    adv=int(input("Digite um numero: "))
    if adv > num:
        print ("É maior!")
    elif adv < num:
        print ("É menor!")
    else:
        print ("Parabéns você acertou!")
