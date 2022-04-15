

def check_fermat(a, b, c, n):
    errado = (a**n) + (b**n)
    if n > 2 and errado == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn'twork.")

check_fermat(2,2,2,2)