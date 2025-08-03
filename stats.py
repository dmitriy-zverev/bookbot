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

def sort_on_num(items):
    print(items["num"])
    return items["num"]

def sort_char_dict(char_dict):
    sorted_char_dict = []
    
    for item in char_dict:
        sorted_char_dict.append({"char": item, "num": char_dict[item]})
    
    sorted_char_dict = sorted(sorted_char_dict, reverse=True, key=sort_on_num)

    return sorted_char_dict
