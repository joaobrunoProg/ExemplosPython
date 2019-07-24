largura=float(input("Digite a largura da parede: "))
altura=float(input("Digite a altura da parede: "))
area=largura*altura
ltinta=area/2
print("Sua parede tem dimensão de {}x{} e sua área é de {:.3f}m².Para pintar sua parede, você precisará de {:.4f}l "
      "de tinta".format(largura,altura,area,ltinta))
