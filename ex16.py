sal=float(input("Qual é o salário do Funcionário? R$"))
aum=sal+(sal*15/100)
print("Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}".format(sal,aum))
