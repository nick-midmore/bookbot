def count_words(s):
    words = s.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        print(file_contents)
        print(count_words(file_contents))

main()
