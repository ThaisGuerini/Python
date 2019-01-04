#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      thais
#
# Created:     10/10/2018
# Copyright:   (c) thais 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Exercício

#1)
def do_twice(f):
     f()
     f()


def print_spam():
    print('spam')

do_twice(print_spam)


#2)
def do_twice (f,x):
     f(x)
     f(x)

def print_spam(x):
     print(x)

do_twice(print_spam, 'bla')


#3)
def do_four(f,x):
     do_twice(f,x)
     do_twice(f,x)


do_four(print_spam,'5')


#4)

do_twice(print_spam,"+ - - - -"), print("+"),
do_four(print_spam,"/"),
print("+"),
do_four(print_spam,"/"),
print("+")

