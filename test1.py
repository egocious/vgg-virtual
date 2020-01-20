
data_structure = {'toke.makinwa@yahoo.com': 102000 , 'sandra.orji@yahoo.com': 12000, 'mohammed.buhari@yahoo.com': 44000, 'shola.badmus@yahoo.com': 49000, 'pius. sydney@yahoo.com': 72000,  'shola.shobowale@yahoo.com': 56000, 'abigail.turko@yahoo.com':592000, 'teni.lawal@yahoo.com': 81000, 'bambam.ortega@yahoo.com': 84000, 'darlington.yaki@yahoo.com': 72000, 'yemi.osibajo@yahoo.com': 37000 }

option = raw_input("Press 1 to create an account \nPress 2 for transactions: ")

if option == "1":
    name = raw_input("Enter your name: ")
    email = raw_input("Enter your email/unique identity: ")
    password = raw_input("Enter your password: ")

    for key in data_structure:  
        if key == email:
            print "You provided an invalid input"
            #*return option  this did not go to option ... how do i send it back to the top?
        else:
            print "Account created"

elif option == "2":
    name = raw_input("Enter your name: ")
    password1 = raw_input("Enter your 6 letter password: ")
    if len(password1) == 6:
        print "Welcome 1" + name
        print "Press 1 to check balance"
        print "Press 2 to deposit"
        print "Press 3 to withdraw"
        print "Press 4 to transfer"
    elif len(password1) > 6:
        print "You are not authorised"
        print "Please create an account with us"
        #*return options did not eeturn
    else:
        print "Password is too short"
        print password1 #this did not go to passwod1 . went to next line instead

    options = raw_input("Press: ")

    if options == "1":
        #key = data_structure[""]
        current_balance = 12222
        print current_balance
        print "Thank you for banking with us"
    elif options == "2":
        #users_balance 
        deposit = int(raw_input("Enter deposit amount >> "))
        new_balance = deposit + current_balance #*not defined
        print "New balance is: %d" %new_balance
        print "Thank you for banking with us" 
    elif options == "3":
        withdrawal = int(raw_input("Enter withdrawal amount >> "))
        new_wbalance = new_balance - withdrawal#* new bal not defined
        if new_balance == 0:
            print "Please deposit some funds"
            #*return deposit
        elif new_balance > 0:
            print "Amount withdrawn: " + withdrawal
            print "New balance is " + new_wbalance
            print "Thank you for banking with us"
        else:
            print "Transaction not complete"
                
    elif options == "4":
        transfer_email = raw_input("Input beneficiary's email >> ")
        transfer_amount = int(raw_input("Input transfer amount >> "))
        #curent_balance = 10000
        beneficiary_balance = 0
        new_ubalance = new_wbalance - transfer_amount
        #add the amount to the beneficiaries account,
        if transfer_amount == 0:
            print "Please input an amount"
        elif transfer_amount > 0:
            print "Your transaction was succesfull and your new account balance is " + new_ubalance
        else:
            print "Unable to complete tranfer"
    else:
        print "Invalid option choice. Please choose between options 1-4"

else: 
    print "HOPE YOU COME BACK SOON"
