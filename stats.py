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

def sorting_chars(chardict):
    return chardict.sort(reverse = True, key = sort_on)