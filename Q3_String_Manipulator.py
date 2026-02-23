#String Manipulation

#user input sentence
sentence = input("Enter a sentence: ")

#original sentence
print("Original sentence: ", sentence)
#Total characters in sentence (with spaces)
with_spaces = len(sentence)
print("Total characters in sentence (with spaces): ", with_spaces)
#Total characters in sentence (without spaces)
without_spaces = len(sentence.replace(" ", ""))
print("Total characters in sentence (without spaces): ", without_spaces)
#Total words
words = sentence.split()
print("words: ", len(words))
#upercase
upper = sentence.upper()
print("Uppercase: ", upper)
#lowercase
lower = sentence.lower()
print("Lowercase: ", lower)
#title case 
title = sentence.title()
print("Title Case: ", title)
#first word
first_word = words[0]
print("First word: ", first_word)
#last word
last_word = words[-1]
print("Last word: ", last_word)
#reversed sentence
reversed_sentence = sentence[::-1]