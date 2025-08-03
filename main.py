def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    return ""

def count_words(book_contents):
    return len(book_contents.split())

def main():
    num_words = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()