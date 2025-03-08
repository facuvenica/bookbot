def count_unique_characters(book):
    """Cuenta los caracteres en un libro"""
    chars = {}

    for i in range(0,len(book)):
        char = book[i].lower()
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1

    return chars
