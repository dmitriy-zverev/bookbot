def get_num_words(book_contents):
    return len(book_contents.split())

def count_characters(book_contents):
    lower_book_contents = book_contents.lower()
    char_dict = {}

    for char in lower_book_contents:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict