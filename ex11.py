valor=float(input("Digite um valor em metros: "))
print("{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm".format(valor/1000,valor/100,valor/10,valor*10,valor*100,valor*1000))
