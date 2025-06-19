from stats import count_num_words, count_num_chars, sort_count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    
    return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_num_words(book_text)
    num_chars = count_num_chars(book_text)

    char_list = sort_count_chars(num_chars)

    print(f"{num_words} words found in the document")
    print(char_list)

if __name__ == "__main__":
    main()
