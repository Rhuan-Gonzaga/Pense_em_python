"""
Como exercício, use o desenvolvimento incremental para escrever uma função chamada hypotenuse, que
devolva o comprimento da hipotenusa de um triângulo retângulo dados os comprimentos dos outros dois
lados como argumentos. Registre cada etapa do processo de desenvolvimento no decorrer do processo.
"""

import math

def hypotenuse(b,c):
    """print(math.hypot(a,b, c))"""
    print(math.sqrt(b**2 + c**2))

hypotenuse(3,4)