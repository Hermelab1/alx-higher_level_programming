#!/usr/bin/python3
if __name__=="__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addition = add(a, b)
    subtraction = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)
    print(f"{a} + {b} = {addition}")
    print(f"{a} - {b} = {subtraction}")
    print(f"{a} * {b} = {multiplication}")
    print(f"{a} / {b} = {division}")
