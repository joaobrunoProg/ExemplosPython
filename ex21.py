from math import sin,tan,cos,radians
angulo=int(input("Digite o ângulo: "))
cos=cos(radians(angulo))
sen=sin(radians(angulo))
tang=tan(radians(angulo))
print("O ângulo de {:.1f} tem o COSSENO de {:.2f}".format(angulo,cos))
print("O ângulo de {:.1f} tem o SENO de {:.2f}".format(angulo,sen))
print("O ângulo de {:.1f} tem o TANGENTE de {:.2f}".format(angulo,tang))
