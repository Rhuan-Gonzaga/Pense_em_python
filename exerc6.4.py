"""
Como um exercício, escreva uma função is_between(x, y, z) que retorne True, se x ≤ y ≤ z, ou False,
se não for o caso.
"""

def is_between(x,y,z):
    if x < y < z:
        return True
    else:
        return False



print(is_between(2,3,5)) #TRUE
print(is_between(5,7,2)) #FALSE
