# Jakeb Brown
# 9/12/2020
# This is an ATM for my intigration assignment
#

# Data Colection
checking_account = int(10750)
savings_account = int(70820)
daily_limit = int(500)

# Card number errors
entered_card = input("Enter your card number >>>")
stored_card = str(1)
card_attempts = int(3)
while (entered_card != stored_card):
    if (card_attempts <= 0):
        print("Attempt maximum exceeded")
        quit()
    card_attempts = card_attempts - 1
    print("Invalid card number. \nAttempts remaining:", card_attempts, "\nPlease try again")
    entered_card = input("Enter your card number >>>")

# Pin number errors
entered_pin = input("Enter your pin number >>>")
stored_pin = str(1234)
pin_attempts = int(3)
while (entered_pin != stored_pin):
    if (pin_attempts == 0):
        print("Attempt maximum excedded")
        quit()
    else:
        pin_attempts = pin_attempts - 1
        print("Invalid pin number. \nAttempts remaining:", pin_attempts, "\nPlease try again")
        entered_pin = input("Enter your pin number >>>")

# Month errors
entered_month = input("Enter the expiration month >>>")
stored_month = str(12)
month_attempts = int(3)
while (entered_month != stored_month):
    if (month_attempts == 0):
        print("Attempt maximum excedded")
        quit()
    else:
        month_attempts = month_attempts - 1
        print("Invalid expiration month. \nAttempts remaining:", month_attempts, "\nPlease try again")
        entered_month = input("Enter the expiration month >>>")

# Year errors
entered_year = input("Enter the expiration year >>>")
stored_year = str(24)
year_attempts = int(3)
while (entered_year != stored_year):
    if (year_attempts == 0):
        print("Attempt maximum excedded")
        quit()
    else:
        year_attempts = year_attempts - 1
        print("Invalid expiration year. \nAttempts remaining:", year_attempts, "\nPlease try again")
        entered_year = input("Enter the expiration year >>>")

# cvn errors
entered_cvn = input("Enter your cvn >>>")
stored_cvn = str(123)
cvn_attempts = int(3)
while (entered_cvn != stored_cvn):
    if (cvn_attempts == 0):
        print("Attempt maximum excedded")
        quit()
    else:
        cvn_attempts = cvn_attempts - 1
        print("Invalid cvn. \nAttempts remaining:", cvn_attempts, "\nPlease try again")
        entered_cvn = input("Enter your cvn >>>")

# What does the customer want to do
print("Your checking account balance is $", format(checking_account, "0.2f"), sep='')
print("Your savings account balance is $", format(savings_account, "0.2f"), sep='')
print("Your withdraw daily limit is $", format(daily_limit, "0.2f"), sep='')
user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))
if (user_want != 1 and user_want != 2):
    print("Invalid response, please try again.")
    user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))
else:
    print("Invalid response please try again.")
    user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))

# Withdraws
if (user_want == 1):
    withdraw_account = int(input("What account would you like to withdraw from. \nChecking = 1, Savings = 2"))
    if (withdraw_account == 1):
        print("Your checking account balance is $", format(checking_account, "0.2f"), sep='')
        checking_withdraw_amount = int(input("How much would you like to withdraw from your checking account? $"))
        if (checking_withdraw_amount > checking_account or checking_withdraw_amount > daily_limit):                     # Checks if you have sufficient funds/under daily limit
            print("You either have insufficient funds or have exceeded the daily limit for withdraws.")
            checking_withdraw_amount = int(input("How much would you like to withdraw from your checking account? $"))
        else:
            checking_account = checking_account - checking_withdraw_amount
            daily_limit = daily_limit - checking_withdraw_amount
            print("Your new checking account balance is $", format(checking_account, "0.2f"), sep='')
            print("Your new daily limit is $", format(daily_limit, "0.2f"), sep='')
            ##user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))
    elif (withdraw_account == 2):
        print("Your savings account balance is $", format(savings_account, "0.2f"), sep='')
        savings_withdraw_amount = int(input("How much would you like to withdraw from your savings account? $"))
        if (savings_withdraw_amount > savings_account or savings_withdraw_amount > daily_limit):                        # Checks if you have sufficient funds/under daily limit
            print("You either have insufficient funds or have exceeded the daily limit for withdraws.")
            savings_withdraw_amount = int(input("How much would you like to withdraw from your savings account? $"))
        else:
            savings_account = savings_account - savings_withdraw_amount
            daily_limit = daily_limit - savings_withdraw_amount
            print("Your new savings account balance is $", format(savings_account, "0.2f"), sep='')
            print("Your new daily limit is $", format(daily_limit, "0.2f"), sep='')
            ##user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))
    else:
        print("Invalid answer.")
        user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))
else:                                                                                                                   # Deposits
    deposit_account = int(input("What account would you like to deposit into? \nChecking = 1, savings = 2"))
    if (deposit_account == 1):
        print("Your checking account balance is $", format(checking_account, "0.2f"), sep='')
        checking_deposit_amount = int(input("How much would you like to deposit? $"))
        checking_account = checking_account + checking_deposit_amount
        print("Your new checking account balance is $", format(checking_account, "0.2f"), sep='')
        ##user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))
    elif (deposit_account == 2):
        print("Your savings account balance is $", format(savings_account, "0.2f"), sep='')
        savings_deposit_amount = int(input("How much would you like to deposit? $"))
        savings_account = savings_account + savings_deposit_amount
        print("Your new savvings account balance is $", format(savings_account, "0.2f"), sep='')
        ##user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))
    else:
        print("Invalid answer.")
        user_want = int(input("Would you like to withdraw or deposit. \nWithdraw = 1, Deposit = 2"))