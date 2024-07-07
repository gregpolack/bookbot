<<<<<<< HEAD
def count_words(book):
    words = book.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        word_count = count_words(file_contents)
        print(word_count)
=======
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
>>>>>>> bf7d7bb9fd6c86c7fe242e303afc1eeb58593c90

if __name__ == "__main__":
    main()