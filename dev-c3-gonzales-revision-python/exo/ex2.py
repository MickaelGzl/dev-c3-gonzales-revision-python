def handlingSentence(sentence):
    return {
        'toLower': sentence.lower(),
        'toUpper': sentence.upper(),
        'length': len(sentence.split(' '))
    }

userSentence = input('Entrez une phrase: ')
print(handlingSentence(userSentence))

