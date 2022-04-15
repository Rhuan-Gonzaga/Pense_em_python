
from __future__ import print_function, division

# here is a mostly-straightforward solution to the
# two-by-two version of the grid.

def do_twice(f):
    f() #3
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ') #5

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams() #4
    do_four(print_posts)

def print_grid():
    do_twice(print_row) #2
    print_beams() #6

print_grid() #1 
    


