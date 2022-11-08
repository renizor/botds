s = input("знак (+, -, *, /): ") 
if s not in ('+', '-', '*', '/'):
    a = float(input("a ="))
b = float(input("b ="))

if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s =="/":
    if b != 0:
     print(a / b)
    else:
        print("деление на 0!")