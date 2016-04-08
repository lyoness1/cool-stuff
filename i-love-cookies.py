"I love  cookies"
"cookies  love I"

#makes a list to store the words and spaces
word_list = []

def make_new_word(lst):
    '''takes a list of chars and creates a word. Adds word to word list'''
    new_word = ''.join(lst)
    word_list.append(new_word)

def find_words(lst):
    '''returns a list of words and spaces in forward order'''
    new_word_chars = []
    for char in lst:
        #adds chars from char list to a new list in order to later create a word from them
        if char != ' ':
            new_word_chars.append(char)
        #if space is found, create a word and add it to the word list, then add spaces to the word list. 
        else: 
            if new_word_chars != []:
                make_new_word(new_word_chars)
            word_list.append(char)
            new_word_chars = []
    #makes the last word if no more spaces are found
    if new_word_chars != []:
        make_new_word(new_word_chars)
    return word_list

#find_words(['a', 'b', 'c', ' ', ' ', 'd', 'e', 'f'])


def reverse(l):
    '''reverses a list'''
    if len(l) == 0: return []
    return [l[-1]] + reverse(l[:-1])


def reverse_words():
    '''reverses the words, including extra spaces'''
    
    original_sentence = raw_input("What sentence would you like to reverse? ")

    #makes a list to store the characters of the sentence
    char_list = [] 
    
    #makes a list of all the characters in the sentence, including spaces
    for x in original_sentence: 
        char_list.append(x) 

    #puts words and spaces in a new list, with any number of spaces added as separate words
    find_words(char_list)
    print word_list

    #reverses the word and space list
    print ''.join(reverse(word_list))

reverse_words()








