"I love  cookies"
"cookies  love I"

word_list = []
char_list = []

def find_words(lst):
    '''returns a list of words and spaces in forward order'''
    if lst == []:
        return word_list
    new_word = "".join(lst[0:lst.index(' ')])
    word_list.append(new_word)
    for char in lst[lst.index(' '):]:
        if char == ' ':
            word_list.append(char)
        else:
            find_words(lst[lst.index(char):])

    #find_words(lst[lst.index(' ':])

find_words(['a', 'b', 'c', ' ', ' ', 'd', 'e', 'f'])

# def reverse(l):
#     '''reverses a list'''
#     if len(l) == 0: return []
#     return [l[-1]] + reverse(l[:-1])


# def reverse_words():
#     '''reverses the words, including extra spaces'''
    
#     original_sentence = raw_input("What sentence would you like to reverse? ")

#     char_list = [] #makes a list to store the characters of the sentence
    
#     #makes a list of all the characters in the sentence
#     for x in original_sentence: 
#         char_list.append(x) 


#     word_list = [] #creates a list to hold the words




    # find_words(char_list) #puts words and spaces in a new list
    # reverse(word_list) #reverses the word and space list

#reverse_words()








