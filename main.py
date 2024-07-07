def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)

        print(f"The number of words in the book is: {word_count}")
        print("=" * 40)
        print("Letter count inside the book:")
        
        for key in char_count:
            print(f"{key} -> {char_count[key]}")

def count_words(book):
    
    words = book.split()
    return len(words)

def count_chars(book):

    char_count = {}
    for letter in book:
        if letter.isalpha():
            letter = letter.lower()
            if letter not in char_count:
                char_count[letter] = 1
            else:
                char_count[letter] += 1
    return char_count 

if __name__ == "__main__":
    main()