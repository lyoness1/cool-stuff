sent = "I love   cookies"

def reverse_sent(sentence):

    words = sentence.split(" ")

    reversed_words = reversed(words)

    print " ".join(reversed_words)

reverse_sent(sent)