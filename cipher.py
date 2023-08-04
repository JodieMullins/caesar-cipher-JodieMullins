encoded = {
    'a': 'f',
    'b': 'g',
    'c': 'h',
    'd': 'i',
    'e': 'j',
    'f': 'k',
    'g': 'l',
    'h': 'm',
    'i': 'n',
    'j': 'o',
    'k': 'p',
    'l': 'q',
    'm': 'r',
    'n': 's',
    'o': 't',
    'p': 'u',
    'q': 'v',
    'r': 'w',
    's': 'x',
    't': 'y',
    'u': 'z',
    'v': 'a',
    'w': 'b',
    'x': 'c',
    'y': 'd',
    'z': 'e',
}

cipher = str.maketrans(encoded) 

user_sentence = str(input('Input message: ')).lower()

user_sentence = user_sentence.translate(cipher)

print('The encrypted sentence is:', user_sentence)