class ATM:
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()

  def menu(self):
    print('-' * 50,'\nHow would you like to proceed.\n1. Create Pin\n2. Change Pin\n3. Deposit\n4. Withdraw\n5. Balance Inquiry\n6. Exit')
    print('-' * 50)
    
    user_input = input('Please entere your choice: ')

    match  user_input :
      case '1' :
        self.create_pin()
      case '2' :
        self.change_pin()
      case '3' :
        self.deposit()
      case '4' :
        self.withdraw()
      case '5' :
        self.check_balance()
      case '6' :
        print('Have a nice day.\nExiting.........')
        exit()
      case _ :
        print(f'INVALID CHOICE !\nPlase Try again')  
        self.menu()

  def create_pin(self):
    if self.pin == '':
      user_pin = input('Please enter your pin: ')
      self.pin += user_pin
      print('Pin created successfully.') 
      self.menu() 
    else:
      print('Pin already created.')    
      self.menu() 

  def change_pin(self):
    if self.pin != '':
      old_pin = input('Enter your old pin: ')
      if old_pin == self.pin :
        self.pin = ''
        self.menu()
      else:
        print('Your pin is incorrect.')
        self.menu() 
    else:
      print('Please create your pin first.')
      self.create_pin()      

  def deposit(self):
    if self.pin != '':
      amount = int(input('Enter your amount: '))
      self.balance += amount
      print(f'₹{amount} added successfully.') 
      self.menu()
    else:
      print('Please create your pin first.')     
      self.menu()

  def withdraw(self):
    if self.pin != '':
      if self.balance > 0 :
        amount = int(input('Enter the amount to withdraw: '))
        if amount > self.balance:
          print('Insufficent Balance.')
          self.menu()
        else:  
          self.balance -= amount
          print(f'₹{amount} withdraw successfull.')
          print(f'Your avaliable balance = {self.check_balance()}')
      else:
        print(f'Your avaliable balance is to low, You can not withdraw money.')    
        self.menu()
    else:
      print('Please create your pin first.')
      self.menu()

  def check_balance(self):
    if self.pin != '':
      print(f'Your avaliable balance is ₹{self.balance}')
      self.menu()  
    else:
      print('Please create your pin first.')
      self.menu()  
   


obj = ATM()
print(obj.balance)