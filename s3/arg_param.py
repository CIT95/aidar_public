#descriptive info for user
print('This program will calculate any mileage reimbursement amount based on the IRS\' rate.')

#run to Y or y
run='Y'

while run == 'Y' or run == 'y':


    #function calculating driven mileage (outer)
    def drivenMileage():
        start = int(input('Please enter your starting mileage: '))
        end = int(input('Please enter your ending mileage: '))
        mileage = end - start
        print('Your mileage total is ' + str(mileage))

        #inner function calculating reimbursement
        def calculateReimbursement (mileage, rate=0.56): #two parameters, mileage variable and rate default
            reimbursement = mileage * rate 
            print('Your reimbursement total is ' + str(format(reimbursement, '.2f')))

        #inner fuction called inside outer function
        calculateReimbursement(mileage) #output reimbursement

    #outer function call
    drivenMileage() #output mileage

    #ask user if he/she wants to run program again and act accordingly
    run = input('Would you like to run this program again? Y/N ')

    if (run != 'y') or (run != 'y'):
        print('Thank you.')

    continue



