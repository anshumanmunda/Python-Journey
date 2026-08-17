'''
Project : To-Do List Manager
The user should be able to:

load previously saved tasks
create a task
view tasks
mark a task as complete
save changes
exit the application

'''
import json

file_name = "to-do-list.json"

def load_tasks():
  try:
    with open(file_name, 'r') as f:
      return json.load(f)

  except FileNotFoundError:  
     print(f"No such file or directory: '{file_name}' ")


def save_tasks(tasks):
  try:  
    with open(file_name, 'w') as f:
      json.dump(tasks, f, indent=4)

  except FileNotFoundError:
    print('Fail to save task.')    



def view_tasks(tasks):
  print()
  tasks_list = tasks["tasks"]

  if len(tasks_list ) == 0:
    print("No task to display.")
  else:  
    print('--------------------------------Your To-Do List:--------------------------------')
    
    for index, task in enumerate(tasks_list):
      status = "[Completed]" if task["complete"] == True else "[Pending]"
      print(f'{index + 1}. {task["description"]} | {status}')
  print()
      

def create_task(tasks):
  description = input('Enter the task description: ').strip()
  
  if description:
    tasks["tasks"].append({"description" : description, "complete": False})
    save_tasks(tasks)
    print('Tasks Saved.....')

  else:
    print('Description can not be empty.')  

def mark_task_complete(tasks):
  view_tasks(tasks)
  try:
    task_number = int(input('Enter the task number to mark as complete: '))

    if 1<= task_number <= len(tasks):
      tasks["tasks"][task_number - 1]["complete"] = True
      save_tasks(tasks)
      print('Marked as complete')
    else:
      print('Invalid task number')

  except ValueError:
    print('Please enter a valid  number.')     

def delete_task(tasks):
  view_tasks(tasks)
  try:
    task_number = int(input('Enter the task number to delete: '))

    if  1 <= task_number <= len(tasks["tasks"]):
      tasks["tasks"].pop( task_number - 1 )
      save_tasks(tasks)
      print(f'Task number:{task_number} deleted.') 

    else: 
      print('Enter a valid task number')  

  except Exception as e:
    print(e)  



def main():
  tasks = load_tasks()

  while True:
    print(" ================================== To-Do List Manager ==================================\n")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == '1':
      view_tasks(tasks)

    elif choice == '2':
      create_task(tasks)

    elif choice == '3':
      mark_task_complete(tasks)

    elif choice == '4':
      delete_task(tasks)

    elif choice == '5':
      print('Good Bye')
      break

    else:
      print("Invalid choice. Please try again.")


# main()
main()

