import sys
from stats import count_words

def count_chars(s):
    values = {}
    for c in s.lower():
        if c not in values:
            values[c] = 0
        values[c] += 1
    return values

def report_chars(d):
    for k in sorted(d, key=d.get, reverse=True):
        if k.isalpha():
            print(f"{k}: {d[k]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()

        print(f"--- Begin report of {sys.argv[1]} ---")
        print(f"{count_words(file_contents)} words found in the document")
        report_chars(count_chars(file_contents))
        print("--- End report ---")

main()
