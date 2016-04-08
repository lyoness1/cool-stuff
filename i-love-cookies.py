"I love  cookies"
"cookies  love I"

def reverse_words():
    '''reverses the words, including extra spaces'''
    original_sentence = raw_input("What sentence would you like to reverse? ")
    char_list = [] #makes a list to store the characters of the sentence
    for x in original_sentence: #makes a list of all the characters in the sentence
        char_list.append(x) 
    print char_list #for debugging purposes
    word_list = [] #creates a list to hold the words
    for item in char_list: #iterates through characters to create words and count spaces
        new_word = "" #creates a string to store each word before adding it to a word list
        space_count = 0
        if item != " ": #executed if character is found
            space_count = 0 #resets space count to zero because we've entered a new word
            new_word += item #creating a word from characters
            char_list = char_list[1:] #making the char_list smaller
        word_list.append(new_word) #adds words to a word list
        if item == " ": #executed if a space is found
            new_word = ""
            space_count += 1
            char_list = char_list[1:]


reverse_words()