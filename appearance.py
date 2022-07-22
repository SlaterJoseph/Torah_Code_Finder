import sys
from collections import defaultdict

def create_dict(script):
    letters = defaultdict(list)
    my_script = open(script, encoding='utf-8')

    for line in my_script:
        for index in range(len(line)):
            letters[line[index]].append(index)

    return letters

def location(letters):
    

    # for key in letters:
        # sys.stdout.buffer.write(key.encode('utf-8'))
    count(letters)

def organize_groups(letters: defaultdict):
    counter = 0
    while all(len(letters.values)) > 0:
        pass 

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
    
location('processed_text\Chumash\Deuteronomy.txt')

    