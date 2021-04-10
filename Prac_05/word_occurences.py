"""
Count the number of times a word appear in a string
"""

"""Grab string from user"""
words_to_count = {}
text = input("Text: ")
words = text.split()

"""Count the number of words in the text """
for word in words:
    count = words_to_count.get(word, 0)
    words_to_count[word] = count + 1

""" Sort words into alphabetical order and list them"""
words = list(words_to_count.keys())
words.sort()

"""Print out the list of words with their respected frequencies"""
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_to_count[word]))
