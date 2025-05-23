import sys
from stats import (
    count_words,
    count_characters,
    chars_dict_to_sorted_list,
)


def get_book_text(book_path):
    with open(book_path, 'r') as f:
        return f.read()


def print_report(book_path, word_count, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char_dict in chars_sorted:
        if not char_dict['char'].isalpha():
            continue
        print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")


def main():
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    # print(f"{word_count} words found in the document")
    char_count = count_characters(book_text)
    # print(f"{char_count} characters found in the document")
    sorted_char_count = chars_dict_to_sorted_list(char_count)
    # print(sorted_char_count)
    print_report(book_path, word_count, sorted_char_count)


if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

main()
