def process_nums(code: str, text: str) -> str:
    parsed_string = ''
    my_file = open(text, 'r', encoding='utf-8')
    for line in my_file:
        sequence = code.split(',')
        count = int(sequence[0]) - 1
        seq_count = 0  # keeps track of where in the sequence we are
        while count < len(line):  # loops through the line
            parsed_string += line[count]  # adds the character at count
            seq_count += 1

            if seq_count == len(sequence):
                seq_count = 0  # resets the sequence once it makes a full loop

            count += int(sequence[seq_count])  # increments count by next number in sequence

    return ''.join(parsed_string.split())  # returns processed code


def find_words(text: str, location: int, length=0) -> str:
    if type(length) != int or length < 0:
        length = 0

    if location < 1:
        return "Location number must be greater then or equal to 1"

    location -= 1
    my_file = open(text, 'r', encoding='utf-8')
    words = list()

    for line in my_file:
        arr = line.split()

    words.append(arr[location])

    if length > 0:
        count = location + 1
        while length > 0:
            words.append(arr[count])
            count += 1
            length -= 1

    return ' '.join(words)

# print(process_nums("54, 453, 90", "../texts/just_char/leviticus.txt"))
# print(find_words("../texts/words/leviticus.txt", 0, "hello"))
