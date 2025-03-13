from stats import get_num_words,letter_count, sort_on, sort_dict, print_info
import sys

def main():
    
    ### Create an error if the main.py function is called without an additional
    ### argument in the cli
    
    n = len(sys.argv)
    if n == 2:
        output = print_info()
        print(output)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
 
    

main()


