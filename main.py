def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    
    return book_text

def main():
    print(get_book_text("books/frankenstein.txt"))

if __name__ == "__main__":
    main()
