def create_heb_set():
    heb_set = set()
    heb_set.add('\u05D0')
    heb_set.add('\u05D1')
    heb_set.add('\u05D2')
    heb_set.add('\u05D3')
    heb_set.add('\u05D4')
    heb_set.add('\u05D5')
    heb_set.add('\u05D6')
    heb_set.add('\u05D7')
    heb_set.add('\u05D8')
    heb_set.add('\u05D9')
    heb_set.add('\u05DA')
    heb_set.add('\u05DB')
    heb_set.add('\u05DC')
    heb_set.add('\u05DD')
    heb_set.add('\u05DE')
    heb_set.add('\u05DF')
    heb_set.add('\u05E0')
    heb_set.add('\u05E1')
    heb_set.add('\u05E2')
    heb_set.add('\u05E3')
    heb_set.add('\u05E4')
    heb_set.add('\u05E5')
    heb_set.add('\u05E6')
    heb_set.add('\u05E7')
    heb_set.add('\u05E8')
    heb_set.add('\u05E9')
    heb_set.add('\u05EA')
    return heb_set

def concat_file(file):
    '''Removes all non alphanumeric characters from the string'''
    import os  # importing os to get the file name
    import sys

    heb_set = create_heb_set()

    curr_file = open(file, 'r', encoding='utf-8')  # opens the file for reading purposes
    new_file = open('processed_text/Chumash/' + os.path.basename(file),'w', encoding='utf-8')  # created a file for the new processed text, places in processde_texts
    for line in curr_file:  # loops through the text file
        new_line = ''
        count = 0
        para = False
        for ch in line:
            # sys.stdout.buffer.write(ch.encode('utf-8'))
            # print('\n')
            if ch == '(':
                para = True
                # print('in para')
                continue
            elif para == True:
                # print('in para')
                if ch == ')': para = False
                continue 
            elif ch == '{':
                # print('in brack')
                count += 1
                continue
            elif count == 1:
                # print('in brack')
                count = 0
                continue
            elif ch not in heb_set:
                continue
            else:
                new_line += ch
            # sys.stdout.buffer.write(new_line.encode('utf-8'))
            # print('\n')
        new_line = new_line.replace('\u05DA', '\u05DB')
        new_line = new_line.replace('\u05DF', '\u05E0')
        new_line = new_line.replace('\u05DD', '\u05DE')
        new_line = new_line.replace('\u05E3', '\u05E4')
        new_line = new_line.replace('\u05E5', '\u05E6')
        new_file.write(new_line)

def process_code(nums, text):
    sequence = nums.split(',')
    parsed_string = ''

    count = int(sequence[0]) - 1
    seq_count = 0  # keeps track of where in the sequence we are
    while count < len(text):  # loops through the line
        parsed_string += text[count]  # adds the character at count

        seq_count += 1

        if seq_count == len(sequence):
            seq_count = 0  # resets the sequence once it makes a full loop

        count += int(sequence[seq_count]) # increments count by next number in sequence

    return parsed_string # returns processed code

def remove_eng(file):
    import os

    my_file = open(file, 'r', encoding='utf-8')
    heb_set = create_heb_set()
    heb_set.add(' ')
    my_loc = open('Eng_Gone/Chumash/' + os.path.basename(file), 'w', encoding='utf-8')
    curr_string = ''
    for line in my_file:
        for ch in line:
            if ch not in heb_set:
                continue
            curr_string += ch
    my_loc.write(" ".join(curr_string.split()))
    

# remove_eng(r'..\base_text\Chumash\Numbers.txt')