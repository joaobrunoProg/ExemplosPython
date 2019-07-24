import random
a1=str(input("Digite o primeiro aluno: "))
a2=str(input("Digite o segundo aluno: "))
a3=str(input("Digite o terceiro aluno: "))

list=[a1,a2,a3]
sorteado = random.choice(list)

print("O aluno sorteado foi {}".format(sorteado))
