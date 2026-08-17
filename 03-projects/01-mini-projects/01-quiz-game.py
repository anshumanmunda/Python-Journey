questions = ('1. Which data structure operates on a "Last-In, First-Out" (LIFO) principle ? ',
'2. In the context of the Internet, what does "HTTP" stand for', 
'3. Which of these is a "primitive" data type in most programming languages', 
'4. Which planet in our solar system is known as the "Red Planet" ?', 
'5. What is the name of the process that converts source code into machine code ?')

options = (' a) Queue\n b) Array\n c) Stack\n d) Linked List',
           ' a) HyperText Transfer Protocol\n b) Hyperlink Text Transforming Process\n c) High-Tech Transfer Protocol\n d) Home Text Transmission Procedure', 
           ' a) String\n b) Integer\n c) List\n d) Dictionary', 
           ' a) Venus\n b) Jupiter\n c) Saturn\n d) Mars', 
           ' a) Interpretation\n b) Compilation\n c) Debugging\n d) Execution')

answers = ['c', 'a', 'b', 'd', 'b']
correct = wrong = 0
print('\n---------------------------- Quiz Game ----------------------------')

i = 0
while(i < 5):
  print('\n',questions[i])
  print(options[i])
  choice  = input("Choose your option: ")
  if choice not in "abcd":
    print('Invalid Option!')
    wrong += 1
  elif (choice == answers[i]):
    correct += 1
  else :
    wrong += 1 
  
  i += 1
  
print('\n--------- Results ------------- \n')
print(f'Correct = {correct}') 
print(f'Wrong = {wrong}') 
