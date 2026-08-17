class Atm:
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()

  def menu(self):
    choice = input('''
    How can I help you ?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Balance Inquiry
    4. Deposit 
    5. Withdraw
    6. Exit    
   ''')  
    
    if choice == '1': # create pin
      self.create_pin()
    
    if choice == '2':  # change pin
      self.change_pin()
    
    if choice == '3':  # Balance Inquiry
      self.balance_inquiry()
    
    if choice == '4':  # Deposit
     self.deposit()
    
    if choice == '5':  # Withdraw
      self.withdraw()
    
    if choice == '6':  # 
      exit()
    
    else:
      print('Invalid choic')
      exit()
  
  def create_pin(self):  # create pin
    user_pin = input("Enter your pin: ")
    self.pin = user_pin
    print("Pin created sucessfully.")
    self.menu()    

  def change_pin(self):  #change pin
    if self.pin == '':
      print("You have not created pin\nPlease create your pin first")
      self.menu()
    else:
      old_pin =  input("Enter your old pin: ") 
      if old_pin == self.pin:
        new_pin =  input("Enter new pin: ") 
        self.pin = new_pin
        print("Pin changed sucessfully")
      else:
        print('Incorrect Pin !')
      self.menu()

  # Balance Inquiry
  def balance_inquiry(self):
    if self.pin == '':
      print('Please generate your pin first.')
    else: 
      print(f"Balance = {self.balance}")
    self.menu() 

  # Deposit
  def deposit(self):
    if self.pin == '':
        print("Please generate your pin first.")
    else:

      pin = input("Enter your pin: ")
      if pin == self.pin:
        amount = int(input("Enter amount: "))
        self.balance +=  amount 
        print("Deposit sucessfull.")
      else:
        print("Incorrect Pin.")  
    self.menu()     

  # withdraw
  def withdraw(self):
    if self.pin == '':
        print("Please generate your pin first.")
    else:
      pin = input("Enter your pin: ")
      if pin == self.pin:
        amount = int(input("Enter amount: "))
        if self.balance >=  amount :
          self.balance = self.balance - amount
          print("Withdraw sucessfull.")
        else:
          print("Insufficent Balance.")
    self.menu()      
     


obj1 = Atm()   