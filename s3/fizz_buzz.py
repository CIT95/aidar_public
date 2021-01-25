#program will tell user if value is divisible by 3 and/or 5 or return the same value if not.

#run to Y or y
run='Y'

while run == 'Y' or run == 'y':

    #define function to determine if the number is divisible by 3 and/or 5
    def fizz_buzz():

        # if val is divisible by 5 and 3 give user input, if not keep running
        if (val % 3 == 0 and val % 5 == 0 ):
            result ='fizzbuzz'

        #if val is divisible by 3 give user input, if not keep running
        elif (val % 3 == 0):
            result = 'fizz'

        #  if val is divisible by 5 give user input, if not keep running
        elif (val % 5 == 0):
            result = 'buzz'

        #if 3 previous conditions are not met, return val
        else:
            result = val

        return result

     #ask input from user and define as integer
    val=int(input('Please enter a number (no decimals): '))

    #calling the function
    result = fizz_buzz()

    print(result)

    #ask user if he/she wants to run program again and act accordingly
    run = input('Would you like to try another number? Y/N ')
    if (run != 'y') or (run != 'y'):
        print('Thank you for playing. Bye.')

    continue

"""
I had trouble with printing the return value,
this link
https://stackoverflow.com/questions/47607515/how-to-print-a-returned-value-in-python
helped a lot.
"""