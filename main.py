def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    
    return book_text

def count_num_words(text):
    words = text.split()
    
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_num_words(book_text)

    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
