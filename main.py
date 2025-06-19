import sys
from stats import count_num_words, count_num_chars, sort_count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    num_words = count_num_words(book_text)
    num_chars = count_num_chars(book_text)
    char_list = sort_count_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char in char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print ("============= END ===============")

if __name__ == "__main__":
    main()
