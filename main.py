


from stats import get_num_words
from stats import get_char_words
from stats import sorting_chars

def get_book_text(path):
    
    with open(path) as f:
        text = f.read()
    return text





def main():

    path = "books/frankenstein.txt"

    book_text = get_book_text(path)
    charwords = get_char_words(get_book_text(path))
    #sorting_chars(charwords)

    print(f"{get_num_words(get_book_text(path))} words found in the document")
    print(f"{get_char_words(get_book_text(path))} characters")

    



if __name__ == "__main__":
    main()
