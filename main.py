def count_words(book):
    words = book.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        word_count = count_words(file_contents)
        print(word_count)

if __name__ == "__main__":
    main()