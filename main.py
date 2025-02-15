def count_words(s):
    words = s.split()
    return len(words)

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
            print(f"'{k}' was found {d[k]} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in document")
        report_chars(count_chars(file_contents))
        print("--- End report ---")

main()
