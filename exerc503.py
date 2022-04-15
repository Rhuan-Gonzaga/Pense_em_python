
def is_triangule():
    if comprimento_1 > (comprimento_2+comprimento_3) or comprimento_2 > (comprimento_1+comprimento_3) or comprimento_3 > (comprimento_1+comprimento_2):
        print("Não pode formar um triangulo")
    else:
        print("É um triangulo")

comprimento_1 = int(input("Digite o 1° comprimento: "))
comprimento_2 = int(input("Digite o 2° comprimento: "))
comprimento_3 = int(input("Digite o 3° comprimento: "))
is_triangule()
