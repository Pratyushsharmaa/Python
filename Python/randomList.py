names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
numberOfItems = len(names)
randomChoice = random.randint(0,numberOfItems-1)
personPaying = names[randomChoice]
print(f"{personPaying} is going to buy the meal today!")