#!/usr/bin/python3
from math import * 

def do_math(a, b):
    print("Sum of inputs: ", add(a, b))
    print("Difference of inputs: ", subtract(a, b))
    print("Division of inputs: ", div(a, b))
    print("Product of inputs: ", mul(a, b))

if __name__=="__main__":
    a=3
    b=5
    do_math(a, b)
