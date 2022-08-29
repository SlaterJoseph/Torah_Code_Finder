def simplify(file: str) -> None:
    import os
    import re
    from hebset import hebset

    hebset = hebset()
    hebset.add(' ')
    curr_file = open(file, 'r', encoding='utf-8')
    new_file = open('../texts/words/' + os.path.basename(file), 'w', encoding='utf-8')

    for line in curr_file:
        new_line = ''
        count = 0
        para = False

        for ch in line:
            if ch == '(':
                para = True
                continue

            elif para:
                if ch == ')': para = False
                continue

            elif ch == '{':
                count += 1
                continue

            elif count == 1:
                count = 0
                continue

            elif ch == 'ch' or ch == '־':
                new_line += ' '

            elif ch not in hebset:
                continue

            else:
                new_line += ch

        new_line = new_line.replace('\u05DA', '\u05DB')
        new_line = new_line.replace('\u05DF', '\u05E0')
        new_line = new_line.replace('\u05DD', '\u05DE')
        new_line = new_line.replace('\u05E3', '\u05E4')
        new_line = new_line.replace('\u05E5', '\u05E6')
        new_line = re.sub(' +', ' ', new_line)
        new_file.write(new_line)


def concat(file: str) -> None:
    import os

    my_file = open(file, 'r', encoding='utf-8')
    new_line = ''

    for line in my_file:
        new_line = "".join(line.split())

    new_file = open('../texts/just_char/' + os.path.basename(file), 'w', encoding='utf-8')
    new_file.write(new_line)


concat('../texts/words/deuteronomy.txt')
concat('../texts/words/esther.txt')
concat('../texts/words/exodus.txt')
concat('../texts/words/genesis.txt')
concat('../texts/words/leviticus.txt')
concat('../texts/words/numbers.txt')
concat('../texts/words/shir.txt')
