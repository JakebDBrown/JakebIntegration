"""This is my integration project, it is a functioning ATM. The program is
able to make withdraws, deposits, transfers, and a prediction for the next
six weeks."""

__author__ = "Jakeb Brown"


def card_info_attempts(entered, stored):
    """This function takes the entered card information and the stored card
    information to make sure it is the same, but if it isn't the user will
    receive a error message and there is a countdown until they have no
    more attempts and the program quits."""
    attempts = 3
    # Starts the countdown of tries
    while entered != stored:
        if attempts != 0:
            attempts -= 1
            print("Invalid card information. \nAttempts remaining: ", attempts)
            print("Please try again.")
            entered = input("")
        else:
            print("Attempt maximum exceeded")
            quit()


def withdraws(account):
    """This function asks how much money someone would like to take out of
    your account and checks to make sure they have sufficient funds as well
    as being under the daily withdraw limit."""
    limit = 500
    print("Your account balance is $", format(account, "0.2f"), sep='')
    print("Your withdraw limit is $", format(limit, "0.2f"), sep='')
    while True:
        try:
            withdraw_amount = int(input("Enter withdraw amount. $"))
            break
        except ValueError:
            print("Error. Must be a whole number.")
    # Checking if the customer has sufficient funds/over daily limit
    while withdraw_amount > account or withdraw_amount > limit:
        print("Insufficient funds or daily limit exceeded.")
        while True:
            try:
                withdraw_amount = int(
                    input("Enter withdraw amount. $"))
                break
            except ValueError:
                print("Error. Must be a whole number.")
    account -= withdraw_amount
    limit -= withdraw_amount
    print("Your new balance is $", format(account, "0.2f"), sep='')
    print("Your new limit is $", format(limit, "0.2f"), sep='')


def deposit(account):
    """This function asks how much someone would like to deposit into
    someone account."""
    print("Your account balance is $", format(account, "0.2f"), sep='')
    while True:
        try:
            deposit_amount = int(input("Enter deposit amount. $"))
            break
        except ValueError:
            print("Error. Must be a whole number.")
    account += deposit_amount
    print("Your new account balance is $", format(account, "0.2f"), sep='')


def transfers(transfer_from, transfer_to):
    """This function asks the user what account they would like to transfer
    the money to then asks what percent they would like to transfer. After
    that the percent is converted into a decimal, which is then used to find
    the amount that is moving"""
    while True:
        try:
            percent = int(input("What percent would you like to transfer? "))
            break
        except ValueError:
            print("Error. Must be a whole number.")
    # Converting the percent given to a decimal and doing the math
    decimal = percent / 100
    amount_moving = transfer_from * decimal
    transfer_from -= amount_moving
    transfer_to += amount_moving
    print("Transfer amount $", format(amount_moving, "0.2f"), sep='')
    print("Your new balance where you transferred money from is $", format(
        transfer_from, "0.2f"), sep='')
    print("Your new balance where you transferred money to is $", format(
        transfer_to, "0.2f"), sep='')


def prediction(account):
    """This function asks the user how many checks they would like to take
    the average of, then takes the average and multiplies it by 6 and adds
    the account balance."""
    total = 0
    while True:
        try:
            number_of_checks = int(input("How many weekly checks for the "
                                         "average? "))
            break
        except ValueError:
            print("Error. Must be a whole number.")
    # Will run for however many checks told
    for i in range(number_of_checks):
        while True:
            try:
                check_amount = int(input("What was the amount of the check"))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        total += check_amount
    # Finds the average
    average = total / number_of_checks
    prediction_amount = account + average * 6
    print("Your 6 week prediction is $", format(prediction_amount, "0.2f"),
          sep='')


def main():
    """This is the main function that runs all the error tests, asks the
    user what they want to do, and does what the user chooses."""
    check_account = 10750
    save_account = 70820

    # Card number errors
    entered_card = input("Enter your card number ")
    stored_card = "1"
    card_info_attempts(entered_card, stored_card)

    # Pin number errors
    entered_pin = input("Enter your pin number ")
    stored_pin = "1234"
    card_info_attempts(entered_pin, stored_pin)

    # Month errors
    entered_month = input("Enter the expiration month ")
    stored_month = str(12)
    card_info_attempts(entered_month, stored_month)

    # Year errors
    entered_year = input("Enter the expiration year ")
    stored_year = str(24)
    card_info_attempts(entered_year, stored_year)

    # cvn errors
    entered_cvn = input("Enter your cvn ")
    stored_cvn = str(123)
    card_info_attempts(entered_cvn, stored_cvn)

    # What does the customer want to do
    print("Checking account $", format(check_account, "0.2f"), sep='')
    print("Savings account $", format(save_account, "0.2f"), sep='')
    print("Withdraw daily limit $500")
    print("Withdraw = 1, Deposit = 2, transfer = 3, prediction = 4")
    while True:
        try:
            user_want = int(input("Would you like to do? "))
            break
        except ValueError:
            print("Error. Must be a whole number.")

    # Withdraws
    if user_want == 1:
        print("Checking = 1, Savings = 2")
        while True:
            try:
                with_account = int(input("What account do you want to "
                                         "withdraw from? "))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        if with_account == 1:
            withdraws(check_account)
        elif with_account == 2:
            withdraws(save_account)
        else:
            print("Invalid response please try again.")

    # Deposits
    elif user_want == 2:
        print("Checking = 1, Savings = 2")
        while True:
            try:
                deposit_account = int(input("Where do you want to deposit the "
                                            "money? "))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        if deposit_account == 1:
            deposit(check_account)
        elif deposit_account == 2:
            deposit(save_account)
        else:
            print("Invalid response please try again.")

    # Transfer
    elif user_want == 3:
        print("Checking = 1, Savings = 2")
        while True:
            try:
                transfer_account = int(input("Where would you like to move the"
                                             " money? "))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        # From savings to checking
        if transfer_account == 1:
            transfers(save_account, check_account)
        # From checking to savings
        elif transfer_account == 2:
            transfers(check_account, save_account)
        else:
            print("Invalid response please try again.")

    # Prediction for 6 weeks
    elif user_want == 4:
        print("Checking = 1 savings = 2")
        while True:
            try:
                prediction_account = int(input("What account is the "
                                               "prediction for? "))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        if prediction_account == 1:
            prediction(check_account)
        elif prediction_account == 2:
            prediction(save_account)
        else:
            print("Invalid response. Please try again.")
    else:
        print("Invalid response, please try again.")


main()
