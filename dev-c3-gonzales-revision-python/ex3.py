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
            if c == '/' and input[index + 1] == '0':
                raise ValueError("Votre entrée contient une division par 0, qui n'est pas authorisée")
            operations.append(actual_number)
            operations.append(c)
            actual_number = ''

        if index == len(input) - 1:
            operations.append(actual_number)
            
    return operations

            

    

userInput = input('Entrer une opération: ')
print(evalUserInput(userInput))