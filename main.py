from stats import *
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(filename):
    word_list = filename.split()
    word_number = len(word_list)
    return word_number

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book")
        sys.exit(1)
    num_words = word_counter(get_book_text(sys.argv[1]))
    print(f"Found {num_words} total words found in the document")
    char_dict = char_counter(get_book_text(sys.argv[1]))
    char_report(char_dict)    
    
    
    # Get the book path from argument
    book_path = sys.argv[1]

    print(f"Processing {book_path}.")



if __name__ == "__main__":
    main()