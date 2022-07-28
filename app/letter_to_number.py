import sys
import os

def letter_to_number(script):
    my_script = open(script, 'r', encoding='utf-8')
    number_ver = open('../number_variants/Chumash/' + os.path.basename(script), 'w')
    curr_string = ''
    for line in my_script:
        for ch in line:
            curr_string += str(one_to_one(ch))
            curr_string += '|'
        # number_seq = number_seq + '|' + str(one_to_one(ch))
        # sys.stdout.buffer.write(number_seq.encode('utf-8'))
    # print(number_seq)
    number_ver.write(curr_string)


def one_to_one(letter):
    if letter == '\u05D0':
        return '1'
    elif letter == '\u05D1':
        return '2'
    elif letter == '\u05D2':
        return '3'
    elif letter == '\u05D3':
        return '4'
    elif letter == '\u05D4':
        return '5'
    elif letter == '\u05D5':
        return '6'
    elif letter == '\u05D6':
        return '7'
    elif letter == '\u05D7':
        return '8'
    elif letter == '\u05D8':
        return '9'
    elif letter == '\u05D9':
        return '10'
    elif letter == '\u05DB' or letter == '\u05DA':
        return '11'
    elif letter == '\u05DC':
        return '12'
    elif letter == '\u05DE' or letter == '\u05DD':
        return '13'
    elif letter == '\u05E0' or letter == '\u05DF':
        return '14'
    elif letter == '\u05E1':
        return '15'
    elif letter == '\u05E2':
        return '16'
    elif letter == '\u05E4' or letter == '\u05E3':
        return '17'
    elif letter == '\u05E6' or letter == '\u05E5':
        return '18'
    elif letter == '\u05E7':
        return '19'
    elif letter == '\u05E8':
        return '20'
    elif letter == '\u05E9':
        return '21'
    elif letter == '\u05EA':
        return '22'
    elif letter == ' ':
        return '_'

# letter_to_number('Eng_Gone\Chumash\Deuteronomy.txt')
# letter_to_number(r'..\Eng_Gone\Chumash\Numbers.txt')