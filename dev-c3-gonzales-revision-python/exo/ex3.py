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
    try:
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

        # now do each operation 1 by 1 until we have only 1 number

        while len(operations) > 1:
            result = None
            if operations[1] == '+':
                result = add(float(operations[0]), float(operations[2]))
                del operations[:3]
                operations.insert(0, result)
            elif operations[1] == '-':
                result = substract(float(operations[0]), float(operations[2]))
                del operations[:3]
                operations.insert(0, result)

        return operations[0]
    except ValueError as e:
        return e

userInput = input('Entrer une opération: ')
print(evalUserInput(userInput))