import sys
from stats import *


def main(filepath):
    words_count = get_num_words(filepath)
    chars_dict = get_char_count(filepath)
    sorted_chars = sort_dict(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        char = char_data["character"]
        count = char_data["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

    
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])


    



