from typing import MutableSet
def Calculator(a=10,b=20):
    print(a,b)

    def add (a,b):
        c= a+b
        return c
    def sub (a,b):
        c = a - b
        return c
    def Mul (a,b):
        c = a * b
        return c
    def div (a,b):
        c = a / b
        return c

    sum = add(a,b)
    print(sum)
    SUB = sub(a, b)
    print(SUB)
    MUL = Mul(a, b)
    print(MUL)
    DIV = div(a, b)
    print(DIV)

Calculator(6,3)