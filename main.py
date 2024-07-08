def main():
    
    with open("books/frankenstein.txt") as f:
        book = f.read()
        
        word_count = count_words(book)
        char_count = count_chars(book)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"The number of words in the book is equal to {word_count}")
        print("=" * 40)
        print("Letter count inside the book:")
        
        for i in range(0, len(char_count)):
            print(f"The {char_count[i]['letter']} character was found {char_count[i]['number']} times.")

        print("--- End report ---")
        

def count_words(book):
    
    words = book.split()
    return len(words)

def sort_on(dict):
    # Funkcja, która posłuży jako paramter do sortowania słownika liter.
    return dict['number']

def count_chars(book):

    char_dict = {}
    char_list = []

    for letter in book:
        if letter.isalpha():
            letter = letter.lower()
            if letter not in char_dict:
                char_dict[letter] = 1
            else:
                char_dict[letter] +=1
    
    for k,v in char_dict.items():
        
        char_count = {}

        char_count['letter'] = k
        char_count['number'] = v

        char_list.append(char_count)

    char_list.sort(reverse=True, key=sort_on)    
    
    return char_list

if __name__ == "__main__":
    main()