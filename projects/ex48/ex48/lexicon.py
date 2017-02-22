def scan(sentence):
    words = sentence.split()
    output = []
    for word in words:
        output.append(categorize(word))

    return output


def categorize(word):
    lexicon_dic = {
        'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
        'verb': ['go', 'stop', 'kill', 'eat'],
        'stop': ['the', 'in', 'of', 'from','at', 'it'],
        'noun': ['door', 'bear', 'princess', 'cabinet'],
    }

    for category, words in lexicon_dic.items():
        if word in words:
            return (category, word)

    return convert_number(word)

def convert_number(word):
    try:
        return ('number', int(word))
    except ValueError:
        return ('error', word)