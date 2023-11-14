def handlingSentence(sentence):
    return {
        'toLower': sentence.lower(),
        'toUpper': sentence.upper(),
        'length': len(sentence.split(' '))
    }

