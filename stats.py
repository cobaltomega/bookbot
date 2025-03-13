import sys

def get_book_text(file):

    with open(file) as f:
        file_contents = f.read()
    return file_contents


def get_num_words():

    file_contents = get_book_text(sys.argv[1])
    words = file_contents.split()
    num_words = len(words)
    return num_words

def letter_count():
    file_contents = get_book_text(sys.argv[1])
    letters = {}
    lower_letter = file_contents.lower()

    for letter in lower_letter:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_dict(dict):
    list_order = []
    for letter, count in dict.items():
        list_order.append({"letter": letter, "count": count})
    list_order.sort(key=sort_on, reverse=True)
    return list_order


def sort_on(dict):

    return dict["count"]
    
def print_info():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{sys.argv[1]}...")

    print("----------- Word Count ----------")
    
    word_count = get_num_words()

    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    l_count = letter_count()
    sorted_chars = sort_dict(l_count)

    for char_dict in sorted_chars:
        letter = char_dict["letter"]
        count = char_dict["count"]
        if letter.isalpha():
            print(f"{letter}: {count}")
    
    print("============= END ===============")