import random

print('\n-------------------- Number Guessing Game --------------------')
chance = 0
while (True):
  print("Guess the number between(1-10)")
  num = random.randint(1,10)
  guess = int(input('Enter a number: '))

  if guess == num :
    chance += 1
    break;
  if guess > num :
    chance += 1
    print(f"Please guess less than {guess}")
  else :  
    chance += 1
    print(f"Please guess more than {guess}")

print(f"You gussed the number in {chance} chance.")  
