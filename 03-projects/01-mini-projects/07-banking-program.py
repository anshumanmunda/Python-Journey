print('---------------- BANKING PROGRAM ----------------')

def show_balance(balance):
  print(f"Your Balance: ₹{balance}\n")

def deposit(balance, amount):
  return balance + amount

def withdraw(balance, amount):
  if balance < amount:
    return -1
  else:
   return balance - amount


balance = 0
while True:
  print('1. Show Balance\n2. Deposit\n3. Withdraw\n4. Exit')
  choice = input('Enter you choce(1-4): ')

  match choice:
    case '1':  # show balance
     show_balance(balance)

    case '2': # deposit balance
      amount = int(input('Enter the amount to deposit: '))
      if amount < 0:
        print("Amount can't be negative")
      else:   
        balance = deposit(balance, amount)
        print(f"Your Balance: ₹{balance}\n")

    case '3': # withdraw balance
      amount = int(input('Enter the amount to withdraw: '))
      if amount < 0:
        print("Withdraw amount can't be negative")
      else:
        x = withdraw(balance, amount)
        if x == -1 :
          print(f"Insufficent Balance\n")
        else:
          balance =  x
          print(f'Remaining balance = ₹{balance}\n')  

    case '4':
      exit()

    case _:
      print('Invalid choice !')  

print('Thank You have a nice day')
