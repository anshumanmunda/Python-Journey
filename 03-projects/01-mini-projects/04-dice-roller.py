import random

dice_art = {
        1 : ('┌───────────┐',  
             '┆           ┆',    
             '┆     ●     ┆',    
             '┆           ┆',    
             '└───────────┘'),
        2 : ('┌───────────┐',  
             '┆  ●        ┆',    
             '┆           ┆',    
             '┆         ● ┆',    
             '└───────────┘'),
        3 : ('┌───────────┐',  
             '┆  ●        ┆',    
             '┆     ●     ┆',    
             '┆         ● ┆',    
             '└───────────┘'),
        4 : ('┌───────────┐',  
             '┆  ●     ●  ┆',    
             '┆           ┆',    
             '┆  ●     ●  ┆',    
             '└───────────┘'),
        5 : ('┌───────────┐',  
             '┆  ●     ●  ┆',    
             '┆     ●     ┆',    
             '┆  ●     ●  ┆',    
             '└───────────┘'),
        6 : ('┌───────────┐',  
             '┆  ●     ●  ┆',    
             '┆  ●     ●  ┆',    
             '┆  ●     ●  ┆',    
             '└───────────┘'),    }

dice = []
total = 0

no_of_dice = int(input('How many dice ?: '))

# adding elements in dice list 
for e in range(no_of_dice):
  dice.append(random.randint(1,6))

# sum of elements of dice list 
for e in dice:
  total += e

# 2 2 3 -> 7

for e in range(no_of_dice):
  for shape in dice_art.get(dice[e]):
    print(shape)
  
print(f"Total = {total}")    


'''
GENERATE Layout: print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
● ┌ ─ ┐ │ └ ┘

┌───────────┐  
┆           ┆    
┆     ●     ┆    
┆           ┆    
└───────────┘
'''
