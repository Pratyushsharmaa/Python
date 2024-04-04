from random import randint
from art import logo

easy_level = 10
difficult_level = 5

##Function to check user's guess against actual answer.
def check_answer(guess, turns, answer):
  if guess>answer:
    print("Your guess is too high!")
    return turns-1
  elif guess<answer:
    print("Your guess is too low!")
    return turns-1
  else:
    print("You guessed the correct number!")

##Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level
  else:
    return difficult_level

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("Guess a number between 1 and 100")
  answer = randint(1,100)
  print(f"The correct answer is {answer}")

  turns = set_difficulty()
#Repeat the guessing functionality if they get it wrong.
  guess = 0
  while(guess!=answer):
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, turns, answer)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return #to exit guessing loop
    elif guess != answer:
      print("Guess again.")

game()
