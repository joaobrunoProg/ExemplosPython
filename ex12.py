num=int(input("Digite um número para ver sua tabuada: "))
print("-"*12)

for i in range(1,11):
    print("{}x{}={}".format(num,i,num*i))

print("-"*12)
