from stats import get_num_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    return ""

def main():
    book_path = "./books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    char_dict = count_characters(book_contents)

    print(f"{num_words} words found in the document")
    print(char_dict)

main()