def get_book_text(file):

    with open(file) as f:
        file_contents = f.read()
    return file_contents


def get_num_words():

    file_contents = get_book_text("books/frankenstein.txt")
    words = file_contents.split()
    num_words = len(words)
    return num_words

def letter_count():
    file_contents = get_book_text("books/frankenstein.txt")
    letters = {}
    lower_letter = file_contents.lower()

    for letter in lower_letter:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_char_count(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(key=sort_on, reverse=True)
    return chars_list

def sort_on(dict):

    return dict["count"]
    




