def get_num_words(book_text):

    count = 0
    bookwords = book_text.split()

    for word in bookwords:
        count += 1
    
    return count

def get_char_words(book_text):

    lower_text = book_text.lower()
    charcount = 0
    mychar = {}

    for char in lower_text:
        if char in mychar:
            temp = mychar[char]
            mychar[char] = temp + 1
        else:
            mychar[char] = 1

    return mychar

def sort_on(dict):
    return dict["num"]

def sorting_chars(cdict):

    char_list = [] 
    for c in cdict: 
        char_list.append(dict(char=c, num = cdict[c] ))

    char_list.sort(reverse = True, key = sort_on)
        
    return char_list


def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")


    for cdict in sorted_chars:
        char = cdict["char"]
        count = cdict["num"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")