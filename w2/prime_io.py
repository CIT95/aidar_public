#this program finds prime numbers in a given range


#ask for values
print('Please type a number (no decimals):')
num1 = input()
print('Thank you! Now please type another number (no decimals):')
num2 = input()

print("The prime numbers between " + num1 + " and " + num2, " are:")

#prime numbers are greater than one and are not composite.
for num in range(int(num1), int(num2) + int(1)): #given range
   if num > 1: #must be greater than one
       for i in range(2, num): #are greater than one and it will check up to the greater given number.
           if (num % i) == 0: #checks if it is composite
               break #if composite checks again
       else: #if not composite then it is prime and prints the number
           print(num)



""""
https://youtu.be/SpTAxH_Geow
https://youtu.be/2p3kwF04xcA
https://www.programiz.com/python-programming/examples/prime-number-intervals
https://linoxide.com/how-tos/programs/basic-python-if-while/
"""
