import sys
from collections import defaultdict


def create_dict(script):
    letters = defaultdict(list)
    my_script = open(script, encoding='utf-8')

    for line in my_script:
        for index in range(len(line)):
            letters[line[index]].append(index + 1)

    return letters


def location(script):
    letters = create_dict(script)
    print(letters['א'])
    print(letters['ב'])
    print(letters['ג'])
    print(letters['ד'])
    print(letters['ה'])
    print(letters['ו'])
    print(letters['ז'])
    print(letters['ח'])
    print(letters['ט'])
    print(letters['י'])
    print(letters['כ'])
    print(letters['ל'])
    print(letters['מ'])
    print(letters['נ'])
    print(letters['ס'])
    print(letters['ע'])
    print(letters['פ'])
    print(letters['צ'])
    print(letters['ק'])
    print(letters['ר'])
    print(letters['ש'])
    print(letters['ת'])

    count(letters)


def count(letters):
    print(len(letters['א']))
    print(len(letters['ב']))
    print(len(letters['ג']))
    print(len(letters['ד']))
    print(len(letters['ה']))
    print(len(letters['ו']))
    print(len(letters['ז']))
    print(len(letters['ח']))
    print(len(letters['ט']))
    print(len(letters['י']))
    print(len(letters['כ']))
    print(len(letters['ל']))
    print(len(letters['מ']))
    print(len(letters['נ']))
    print(len(letters['ס']))
    print(len(letters['ע']))
    print(len(letters['פ']))
    print(len(letters['צ']))
    print(len(letters['ק']))
    print(len(letters['ר']))
    print(len(letters['ש']))
    print(len(letters['ת']))


# location('processed_text/Chumash/All.txt')
