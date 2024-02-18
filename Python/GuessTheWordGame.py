#Hangman is a guessing game for two or more players. One player thinks of a word, phrase, or sentence and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses.

#List of words
word_list = ["aardvark", "baboon", "camel"] 


import random #choose a random word from the list
chosen_word = random.choice(word_list)

print(f"Hello, the solution is {chosen_word}")
display = [] #display blank char for each letter in the word
for letter in chosen_word:
  display += "_"
print(display)
while "_" in display: #traverse until all letters are guessed
  
  guess = input("Guess a letter: ").lower()
  
  
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  
  print (display)
