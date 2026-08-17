'''
Project : Random Password Generator
The generator asks the user for:

Password length
Uppercase characters
Special characters
Digits

'''
import random
import string


def generate_password():
  length = int( input( 'Enter the desired password length: ' ).strip() ) 

  if length < 4:
    print("Password length must be at least 4 characters.")
    return

  include_uppercase = input( 'Include uppercase letters?' \
  '\n(yes/no): ').lower().strip()

  include_spacial = input( 'Include spacial characters?' \
  '\n(yes/no): ').lower().strip()

  include_digits = input( 'Include digits characters?' \
  '\n(yes/no): ').lower().strip()



  lower = string.ascii_lowercase
  uppercase = string.ascii_uppercase if include_uppercase == 'yes' else ''
  digits = string.digits if include_digits == 'yes' else ''
  spacial = string.punctuation  if include_spacial == 'yes' else ''

  all_characters = lower + uppercase + digits + spacial

  required_characters = []

  if include_uppercase == 'yes':
    required_characters.append(
      random.choice(uppercase)
    ) 

  if include_digits == 'yes':
    required_characters.append(
      random.choice(digits)
    ) 

  if include_spacial == 'yes':
    required_characters.append(
      random.choice(spacial)
    ) 

  remaning_characters = length - len(required_characters)
  password = required_characters

  for _ in range(remaning_characters):
    character = random.choice(all_characters)

    password.append(character)

  random.shuffle(password)

  string_password = ''.join(password)
  print(f'Your password: {string_password}')



generate_password()
