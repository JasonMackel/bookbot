

import sys
from stats import get_num_words
from stats import get_char_words
from stats import sorting_chars
from stats import print_report

def get_book_text(path):
    
    with open(path) as f:
        text = f.read()
    return text





def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path,"r") as f:
            book_contents = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: No permission to read '{path}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


    book_text = get_book_text(sys.argv[1])
    

    print_report(path,get_num_words(get_book_text(path)),sorting_chars(get_char_words(get_book_text(path))))

    

if __name__ == "__main__":
    main()
