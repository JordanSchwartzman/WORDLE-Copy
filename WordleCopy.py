from termcolor import colored 
import random
from spellchecker import SpellChecker

set_of_words = ["squib", "spark", "squab", "anger", "tired", "angel", "dense", "titan", "frost", "frame", "blunt", "flare", "array", "mouse", "fries", "phone", "pizza", "index", "buzzy", "timed", "house", "arson"]

#chooses a random word
word = random.choice(tuple(set_of_words))

print("Wordle Copy")

spell = SpellChecker()

#spell check
def check(word):
  if word == spell.correction(word):
    return True
  else:
    return False

for s in range(2):
  print("")
  
all_lists = []
attempts = 0

#checks for number of attempts, and begins to create a block grid to match your attempt problems. 
while attempts < 7:
  blocks = []
  print("")
  u_input = input("Enter a 5-letter word: ")
  user_input = u_input.lower()
  if check(user_input) != True:
    print("invalid")
  if check(user_input) == True:
    if len(user_input) > 5:
      print("invalid")
    elif len(user_input) < 5:
      print("invalid")
    elif user_input == word:
      u_won = "You Win!"
      win = colored(u_won, 'green')
      for x in range(5):
        blocks.append("🟩")
      all_lists.append(blocks)
      print(colored(user_input, 'green'))
      print(win)
      print(f'{attempts}/6 tries')
      break
    else:
      for a in range(5):
        if word[a] == user_input[a]:
          user_letter_one = colored(user_input[a], 'green')
          blocks.append("🟩")
          print(user_letter_one, end="")
        elif user_input[a] in word:
          user_letter_two = colored(user_input[a], 'yellow')
          blocks.append("🟨")
          print(user_letter_two, end="")
        elif user_input[a] not in word:
          user_letter_three = colored(user_input[a], 'white')
          blocks.append("⬜")
          print(user_letter_three, end="")
    attempts = attempts + 1  
  if len(blocks) == 5:
    all_lists.append(blocks)
  
print(" ")
for i in all_lists:
  print(" ".join(i))
  
if attempts > 6:
  print(f'{attempts - 1}/6 tries')
  print(" ")
  print(f'The word was {word}')
  
