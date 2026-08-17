'''Python credit card validator program

1. Remove any '-' or ' '
2. Add all digits in the odd places from right to left
3. Double every second digit from right to left. (If result is a two-digit number, add the two-digit number together to get a single digit.)
4. Sum the totals of steps 2 & 3
5. If sum is divisible by 10, the credit card # is valid
'''

# ---------- step 1 -----------
card_num = input("Enter your credit card number: ").replace('-', '').replace(' ', '')

# ---------- step 2 -----------
sum_of_odd = 0
for e in card_num[::-2] :
   sum_of_odd += int(e) 

# ---------- step 3 -----------
sum_of_even = 0
for e in card_num[-2::-2]: 
  doubled = int(e) * 2 

  if doubled > 9:
    doubled = (doubled % 10) + (doubled // 10)
  sum_of_even += doubled


# ---------- step 4 -----------
total_sum = sum_of_even  + sum_of_odd
if total_sum % 10 == 0:
  print(f'Valid credit card number.')
else:
  print(f'Invalid credit card number.')



'''
Test data
Test Credit Card Account Numbers
American Express 378282246310005
American Express 371449635398431
American Express Corporate 378734493671000
Australian Bankcard 5610591081018250
Diners Club 30569309025904
Diners Club 38520000023237
Discover 6011111111111117
Discover 6011000990139424
'''
