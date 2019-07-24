km=int(input("Digite o total de kilômetros percorridos: "))
dias=int(input("Digite o total de dias de aluguel do carro: "))
total= (km*0.15) + (60*dias)
print("O valor total a pagar será de {:.2f}".format(total))
