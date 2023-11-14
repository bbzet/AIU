import os 
a = None
b = None

while(a == None and b == None):
    try:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
    except ValueError:
        print("Ошибка. Введите число.")


def multiplication(a, b):
    return a * b 

def division(a, b):
    if b == 0:
        return "На ноль делить нельзя."
    else:
        return a / b

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

inputOperation = input("""
       1- Multiplication (*)
       2- Division (/)
       3- Subtraction (-)
       4- Addition (+)
    """)
os.system('cls')

result = None 

match inputOperation:
    case "*":
        result = multiplication(a, b)

    case "/":
        result = division(a, b)

    case "-":
        result = substraction(a, b)

    case "+":
        result = addition(a, b)
    case _:
        print("WRONG OPERATION SIGN!!!")

if result != None:
    print(f'{a} {inputOperation} {b} = {result}')
