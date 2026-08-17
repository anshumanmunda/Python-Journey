import random 

print("------------------ Rock, Paper, Scissor Game ------------------")

options = ('rock', 'paper', 'scissor')
count = 0
win = 0

while(count < 3):
  player1 = random.choice(options)
  player2 = input('\nYour Turn : ').lower()

  if player2 not in options:
    print('Invalid choice\nSelect either (rock, paper or scissor)')
    

  match player1 :
    case 'rock':
      if player2 == 'rock':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> Tie')
      
      elif player2 == 'paper':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> You Won')
        win += 1
        
      elif player2 == 'scissor':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> You lose')

    case 'paper':
      if player2 == 'rock':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> You lose')
      
      elif player2 == 'paper':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> Tie')
      
      elif player2 == 'scissor':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> You won')
        win += 1

    case 'scissor':
      if player2 == 'rock':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> You won')
        win += 1
      
      elif player2 == 'paper':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> You lose')
      
      elif player2 == 'scissor':
        print(f'\nComputer: {player1}')
        print(f'You: {player2}')
        print('Result -> Tie')
  
  count += 1  
print(f'\nIn best of 3 you won {win} times.')    
      
    
    

