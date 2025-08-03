from stats import get_num_words, count_characters, sort_char_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    return ""

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    char_dict = count_characters(book_contents)
    sorted_char_dict = sort_char_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char in sorted_char_dict:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    
    print("============= END ===============")

main()