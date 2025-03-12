from stats import get_num_words,letter_count, sort_on, sort_char_count

def main():
    l_count = letter_count()
    sorted_chars = sort_char_count(l_count)
    print(sorted_chars)



main()


