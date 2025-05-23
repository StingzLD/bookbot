def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    chars = {}

    for char in book_text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars


def chars_dict_to_sorted_list(d):
    list_to_sort = []

    for key in d:
        list_to_sort.append({"char": key, "count": d[key], })

    return sorted(list_to_sort, key=lambda k: k['count'], reverse=True)
