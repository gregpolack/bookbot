def count_num_words(text):
    words = text.split()
    
    return len(words)

def count_num_chars(text):
    chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars

def sort_on(dict):
    return dict["num"]

def sort_count_chars(chars):
    char_dicts = []
    for char in chars:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = chars[char]
        char_dicts.append(char_dict)
    
    char_dicts.sort(reverse=True, key=sort_on)
    
    return char_dicts