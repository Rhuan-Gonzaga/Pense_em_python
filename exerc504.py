"""
O saida dessa função é 6. A função vai ser executada duas vezes
na primeira 3 vai valer 2 
s vai ficar 3

na segunda 2 vai valer 1
s vai fcr 3 

"""

def recurse(n, s):
    if n == 0:
     print(s) #3 #6
    else:
     recurse(n-1, n+s) #2 #1 #0 
   
     
recurse(3, 0)
