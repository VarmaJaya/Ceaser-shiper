def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c = a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c= a/b
    return c
def mod(a,b):
    c=a%b
    return c
opertaion = input("Please select the operation : +, -, /, *, % : ")
number_1= int(input("Please enter your first number : "))
number_2= int(input("Please enter your second number: "))
if opertaion == "+":
    print(add(a=number_1, b=number_2))
elif opertaion == "-":
    print(sub(a=number_1, b=number_2))
elif opertaion == "*":
    print(mul(a=number_1, b=number_2))
elif opertaion == "/":
    print(div(a=number_1, b=number_2))
elif opertaion == "%":
    print(mod(a=number_1, b=number_2))
else:
    print("wrong operation")
