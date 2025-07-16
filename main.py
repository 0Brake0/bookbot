import sys

def get_book_text(path_to_file):
    with open (path_to_file, "r") as f:
        file_contents = f.read()    
    return file_contents

from stats import count_words
from stats import count_characters
from stats import get_sorted_character_list

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    file_contents = get_book_text(path)
    count_words(file_contents)
    count_characters(file_contents)
    final_list = get_sorted_character_list(count_characters(file_contents))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")
    for item in final_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    return
    
main()