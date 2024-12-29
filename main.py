def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

        report = build_report(path, file_contents)

        print(report)


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


def sort_on(dict):
    return dict["count"]


def sort_dict(data):
    sorted = []
    d = {}
    for char, count in data.items():
        if char.isalpha():
            d = {'char': char, 'count': count}
            sorted.append(d)

    sorted.sort(reverse=True, key=sort_on)

    return sorted


def build_report(path, book):
    report = f"--- Begin report of {path} ---\n"

    n_words = len(book.split())
    count = count_unique_characters(book)
    count = sort_dict(count)

    report += f"\n{n_words} words found in the document\n"

    for element in count:
        char, num = element['char'], element['count']
        report += f"\nThe '{char}' character was found {num} times"

    report += "\n\n--- End report ---"
    return report

main()