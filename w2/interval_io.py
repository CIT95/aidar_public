#this program compares two values and/or sorts them.


#ask for values
print('Please type a number (no decimals):')
num1 = input()
print('Thank you! Now please type another number (no decimals):')
num2 = input()

#comparing for greater than
if str(num1) > str(num2):
    print(str(num1) + ' is greater than ' + str(num2))  

#if not greater than, then sort in ascending order
else:
    print('The ascending order for the range of the given numbers is:')
    while int(num1) <= int(num2):
        print(num1)
        num1 = int(num1) + int(1)
        

 
 
