def factorielle(n):
    try:
        if not n.isdigit():
            raise ValueError("Votre entrée n'est pas un nombre entier")
        result = 1
        n = int(n)
        while n > 1:
            result = result * n
            n = n-1
        return result
    except ValueError as e:
        return e

number = input('Saisissez un nombre entier: ')
print(factorielle(number))
