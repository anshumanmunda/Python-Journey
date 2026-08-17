import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {0: ("   ",
                    "   ",
                    "   "),
              1: (" o ",
                    "   ",
                    "   "),
              2: (" o ",
                    " | ",
                    "   "),
              3: (" o ",
                    "/| ",
                    "   "),
              4: (" o ",
                  "/|\\",
                    "   "),
              5: (" o ",
                    "/|\\",
                    "/  "),
              6: (" o ",
                    "/|\\",
                    "/ \\")}

def display_man(wrong_guesses):
  print('**********')
  for lines in hangman_art[wrong_guesses]:
    print('  ',lines)
  print('**********')

def display_hint(hint):
  print(' '.join(hint))

def display_answer(answer):
    print(' '.join(answer))

def main():
  answer = random.choice(words)
  hint = ['_'] * len(answer)
  wrong_guesses = 0
  gussed_letters = set()
  is_running = True

  while is_running:
    display_man(wrong_guesses)
    display_hint(hint)
    display_answer(answer)
    guess = input("Enter a letter:" ).lower()

    if guess in answer:
      for i in range(len(answer)):
        if guess == answer[i]:
           hint[i] = guess
    

if __name__ == '__main__':
  main() 

# Incomplete