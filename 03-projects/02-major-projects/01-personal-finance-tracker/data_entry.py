from datetime import datetime

date_format = "%d-%m-%Y"
categories = {
  "I": 'Income',
  "E": "Expense"
}

def get_date(prompt, allow_default=False):
  date_str = input(prompt)

  if allow_default and not date_str:
    return datetime.today().strftime(date_format)

  try:
    valid_date = datetime.strptime(date_str, date_format)
    return valid_date.strftime(date_format)
  
  except ValueError:
    print("Invalide date formate!\nPlease enter a valid date: 'dd-mm-yyyy'")

    return get_date(prompt, allow_default)



def get_amount()->float:
  try:
    amount = float( input("Enter the amount: ") )
    if amount < 0:
      raise ValueError('Amount must be greater than 0')
    return amount 
    
  except ValueError as e:
    print(e)  
    return amount 


def get_category():
  category = input("Enter the catogery\n'I': Income\n'E': Expense\nSelect(I/E): ").upper()

  if category in categories.keys():
    return categories[category]

  print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")

  

def get_description():
  return input('Enter description (optional): ')