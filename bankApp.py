bankData = {"username": {"email": 'toke.makinwa@yahoo.com',"current_bal": 102000 },
"username": { "email": 'sandra.orji@yahoo.com', "current_bal": 12000 },    
"username": { "email": 'mohammed.buhari@yahoo.com', "current_bal": 44000 },
"username": { "email": 'shola.badmus@yahoo.com', "current_bal": 49000 },   
"username": { "email": 'pius.sydney@yahoo.com', "current_bal": 72000 } }

option = raw_input("Press 1 To create an account \nPress 2 for transactions: ")

if option == "1":
    name = raw_input("Enter your name: ")
    email_add = raw_input("Enter your email/unique identity: ")
    password = raw_input("Enter your password: ")
    if bankData['username']['email'] == email_add:
        print name + ", Invalid input! Email already in use" 
    else:
        print name + ", Your account has been created"
        print "Press 1 to check your balance"
        print "Press 2 to deposit"
        print "Press 3 to withdraw"
        print "Press 4 to transfer"

elif option == "2":
    name = raw_input("Enter your name: ")
    password1 = raw_input("Enter your 6 letter password: ")
    if len(password1) == 6:
        print "Welcome Back " + name
        print "Press 1 to check your balance"
        print "Press 2 to deposit"
        print "Press 3 to withdraw"
        print "Press 4 to transfer"
    elif len(password1) > 6:
        print "You are not authorised"
        print "Please create an account with us"
        name = raw_input("Enter your name: ")
        email_add = raw_input("Enter your email/unique identity: ")
        password = raw_input("Enter your password: ")
    else:
        print "Password is too short"

else: 
    print "WRONG CODE. PLEASE INPUT 1 OR 2"
    new_option = raw_input("Press 1 To create an account \nPress 2 for transactions: ")

options = raw_input("Press: ")

if options == "1":
    for key in bankData:
        current_balance = bankData['username']['current_bal'] 
        print current_balance 
        print "Thank you for banking with us"
    
elif options == "2":
    deposit = int(raw_input("Enter deposit amount >> "))
    deposit += bankData['username']['current_bal'] 
    print "New balance is: NGN %d" %deposit
    print "Thank you for banking with us"

elif options == "3":
    withdrawal = int(raw_input("Enter withdrawal amount>> "))
    if bankData['username']['current_bal'] == 0:
        print "Please deposit some funds"
        deposit = int(raw_input("Enter deposit amount>> "))
    elif bankData['username']['current_bal'] > 0:
        new_wbalance = bankData['username']['current_bal'] - withdrawal
        print "Amount withdrawn: NGN " + str(withdrawal)
        print "New balance is NGN " + str(new_wbalance)
        print "Thank you for banking with us"
    else:
        print "Transaction not complete"

elif options == "4":
        transfer_email = raw_input("Input beneficiary's email: ")
        transfer_amount = int(raw_input("Input transfer amount >> "))
        beneficiary_balance = 0 + transfer_amount
        print "Beneficiary balance is: NGN %s" %beneficiary_balance
        new_balance = bankData['username']['current_bal'] - transfer_amount
        if transfer_amount == 0:
            print "Please input an amount"
        elif transfer_amount > 0:
            print "Your transaction was succesfull and your account balance is NGN " + str(new_balance)
        else:
            print "Unable to complete tranfer"
else:
        print "Invalid option choice. Please choose between options 1-4"

        

