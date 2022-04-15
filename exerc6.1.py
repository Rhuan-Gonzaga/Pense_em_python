def b(z):
    prod = a(z, z) #3°valor/passo: 9,9   
                   #4°passo: cahama a minha função A passando os valores 9,9
    print(z, prod) #7°passo: primeiro saida 9, 90
    return prod #8°passo: retorna 90 pro meu square da função C

def a(x, y): # (9, 9)
    x = x + 1 # 5°passo: soma = 10
    return x * y #6°passo: 10 * 9 retorna a multiplicação p variavel prod na função B

def c(x, y, z): #(1, 5, 3)
    total = x + y + z #1°paso: total = 9
    square = b(total)**2 #2°passo: chama a minha função b passando o valor (9) 
                         #9° passo: square recebe 90**2 = 8100 
    return square #10° passo: retorna 8100 p minha segunda saida 

x = 1
y = x + 1
print(c(x, y+3, x+y)) #0°passo: Inicio da chamada(1, 5, 3)  
                      #Segunda saida Ultimo passo