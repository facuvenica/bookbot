from stats import count_unique_characters

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        file_contents = f.read()

        report = build_report(sys.argv[1], file_contents)

        print(report)


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
    report = f"============ BOOKBOT ============\nAnalyzing book found at {path}\n"

    n_words = len(book.split())
    count = count_unique_characters(book)
    count = sort_dict(count)

    report += f"----------- Word Count ----------\nFound {n_words} total words\n"
    report += f"--------- Character Count -------\n"

    for element in count:
        char, num = element['char'], element['count']
        report += f"\n{char}: {num}"

    report += "\n\n--- End report ---"
    return report

main()