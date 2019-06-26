import asyncio
import re
import time

# print('******************************************')
# print('**************** Scrabble ****************')
# print('******************************************')
import pandas

from DicoLinkParser import word_exists

_voy = ['a', 'e', 'i', 'o', 'u', 'y']
_no_double = ['h', 'j', 'q', 'v', 'w', 'x']  # regex..
_voy_double = ['a', 'e']  # ...

_letters = []
_nb = 0
_dict = {}
_str_empty = ''

_all_words = {}


def stats():
    for letter in _letters:
        _dict[letter] = _letters.count(letter)
    print(_dict)


def clean_phrase(phrase):
    cleaned = re.sub('[^A-Za-z]', '', phrase)
    return cleaned.upper()


def input_letters():
    phrase = str(input('Saisir lettres : \r\n ==> '))
    phrase = clean_phrase(phrase)
    nb_letters = len(phrase)
    if nb_letters > 0:
        print('letters : ', phrase, ' (', nb_letters, ')')
        for letter in phrase:
            _letters.append(letter)
        # print(_letters)


def is_voy(letter):
    return _voy.__contains__(letter.lower())


def extract_word(letter1, letter2):
    if letter2 is None:
        return _str_empty

    if len(letter2) == 1:
        if letter1 == letter2:
            # print(letter1, ' = ', letter2, '==>', is_voy(letter1), ' ', not _voy_double.__contains__(letter1.lower()))
            if is_voy(letter1) and not _voy_double.__contains__(letter1.lower()):
                return _str_empty
            if not is_voy(letter1) and _no_double.__contains__(letter1.lower()):
                return _str_empty
        else:
            return str(letter1 + letter2)
    else:
        # print(letter2, ' ', letter1, ' ', letter2.count(letter1), ' >= ? ', _dict[letter1])
        if letter2.count(letter1) >= _dict[letter1]:
            return []
        else:
            return [str(letter1 + letter2), str(letter2 + letter1)]


def display():
    print()
    for k in range(2, len(_letters) + 1):
        print(k, '==>', _all_words.get(k), '[', len(_all_words.get(k)), ']')
    print()

    _max = 0
    for k in range(2, len(_letters) + 1):
        if len(_all_words.get(k)) > _max:
            _max = len(_all_words.get(k))

    data = {}
    for k in range(2, len(_letters) + 1):
        temp = _all_words.get(k)
        for i in range(len(_all_words.get(k)) + 1, _max + 1):
            temp.append('x')
        data[k] = temp

    dframe = pandas.DataFrame(data)
    dframe.index = dframe.index + 1
    print(dframe)
    print()


async def check_words(all_words=True):
    stats()
    for n in range(2, len(_letters) + 1):
        combined = []

        print()
        print(f'{n}.')

        if n == 2:
            for i in range(0, len(_letters)):
                for j in range(0, len(_letters)):
                    if i != j:
                        w = extract_word(_letters[i], _letters[j])
                        print(f'{w}.', end=' ')
                        if not w == _str_empty and not combined.__contains__(w):
                            if all_words or word_exists(w):
                                combined.append(w)
                                # print(f'{w}..ok')
        else:
            for i in range(0, len(_letters)):
                for j in range(0, len(_all_words[n - 1])):
                    ws = extract_word(_letters[i], _all_words[n - 1][j])
                    if len(ws) > 0:
                        for w in ws:
                            print(f'{w}.', end=' ')
                            if not combined.__contains__(w):
                                if all_words or word_exists(w):
                                    combined.append(w)
                                    # print(f'{w}..ok')

        # combined.sort()
        _all_words[n] = combined

    display()


def show_time():
    # print('************************')
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S", named_tuple)  # %m/%d/%Y,

    print('******* Scrabble *******')
    print('*******', time_string, '*******')
    # print('************************')


def scrabble():
    show_time()
    input_letters()

    if len(_letters) == 0:
        print('no letters! bye.')
    else:

        # print('****************************************')
        print('**************** words.. ***************')
        start_ms = int(round(time.time() * 1000))

        asyncio.run(check_words(False))

        end_ms = int(round(time.time() * 1000))
        print('time elapsed : ', int(round((end_ms - start_ms) / 1000)), 's.')
        # print('****************************************')


if __name__ == '__main__':
   scrabble()
   input("Appuyer sur ENTER pour quitter le programme.")
