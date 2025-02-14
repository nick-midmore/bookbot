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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        print(file_contents)
        print(count_words(file_contents))
        print(count_chars(file_contents))

main()
