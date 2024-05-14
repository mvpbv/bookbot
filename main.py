




def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print_report(num_chars)
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    new_text = text.lower()
    new_text = list(new_text)
    chars_dict = {}
    for char in new_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_values(a):
    return a[1]

def print_report(chars_dict):
    sorted_tuples = sorted(chars_dict.items(), key=sort_values, reverse=True)
    new_dict = dict(sorted_tuples)
    
    for key, value in new_dict.items():
        if key.isalpha():
            print(f"The {key} character was found {value} times")
main()