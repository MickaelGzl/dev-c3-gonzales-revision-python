import re


def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divise(a, b):
    return a / b
    
def verifyInput(input):
    return re.match(r'^[0-9\.\+\-\*\/]+$', input)

def evalUserInput(input):
    if not verifyInput(input):
        raise ValueError("Votre entrée contient des caractères non valide pour une opération")
    operations = []
    actual_number = ''
    for index, c in enumerate(input):
        if c.isdigit() or c == '.':
            actual_number += c
        else:
            operations.append(actual_number)
            operations.append(c)
            actual_number = ''

        if index == len(input) - 1:
            operations.append(actual_number)

    i = 0

    # do first all * and / opérations. remove numbers and op and add result

    while i < len(operations) -1:
        if operations[i] == '*':
            result = multiply(float(operations[i - 1]), float(operations[i + 1]))
            del operations[i - 1: i+2]
            operations.insert(i-1, result)
        if operations[i] == '/':
            if(operations[i + 1] == 0):
                raise ValueError("Impossible de réaliser une divivion par 0")
            result = divise(float(operations[i - 1]), float(operations[i + 1]))
            del operations[i - 1:i+2]
            operations.insert(i-1, result)
        else:
            i = i+1
    
    
    

    return operations

            

    

userInput = input('Entrer une opération: ')
print(evalUserInput(userInput))