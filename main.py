import sys
from stats import get_num_words
from stats import get_chars_dict
from stats import get_sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = get_sorted_dict(chars_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in sorted_chars_dict:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")


main()