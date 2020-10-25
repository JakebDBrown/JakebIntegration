# Jakeb Brown
# 9/12/2020
# This is an ATM with withdraws, deposits, transfers, and a prediction for 6 weeks
#

def card_info_attempts(givin, stored):
	attempts = 3
	while (givin != stored):
		if (attempts != 0):
			attempts -= 1
			print("Invalid card. \nAttempts remaining: ", attempts)
			print("Please try again.")
			givin = input(">>> ")
		else:
			print("Attempt maximum exceeded")
			quit()
	
# Card number errors
entered_card = input("Enter your card number >>>")
stored_card = "1"
card_info_attempts(entered_card, stored_card)

# Pin number errors
entered_pin = input("Enter your pin number >>>")
stored_pin = "1234"
card_info_attempts(entered_pin, stored_pin)

# Month errors
entered_month = input("Enter the expiration month >>>")
stored_month = str(12)
card_info_attempts(entered_month, stored_month)

# Year errors
entered_year = input("Enter the expiration year >>>")
stored_year = str(24)
card_info_attempts(entered_year, stored_year)

# cvn errors
entered_cvn = input("Enter your cvn >>>")
stored_cvn = str(123)
card_info_attempts(entered_cvn, stored_cvn)

# Account Info
checking_account = 10750
savings_account = 70820
daily_limit = 500

# What does the customer want to do
print("Your checking account balance is $", format(checking_account, "0.2f"), sep='')
print("Your savings account balance is $", format(savings_account, "0.2f"), sep='')
print("Your withdraw daily limit is $", format(daily_limit, "0.2f"), sep='')
print("Withdraw = 1, Deposit = 2, transfer = 3, prediction = 4")
user_want = int(input("Would you like to do? "))

# Withdraws
if(user_want == 1):
	print("Checking = 1, Savings = 2")
	withdraw_account = int(input("What account would you like to withdraw from. "))
	if (withdraw_account == 1):
		print("Your checking account balance is $", format(checking_account, "0.2f"), sep='')
		print("How much would you like to withdraw?")
		checking_withdraw_amount = int(input("$"))
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
	else:
		print("Invalid answer.")
		#print("Withdraw = 1, Deposit = 2, transfer = 3, prediction = 4")
		#user_want = int(input("Would you like to do? ")) 
			
# Deposits
elif (user_want == 2):                                                                                                              
	deposit_account = int(input("What account would you like to deposit into? \nChecking = 1, savings = 2 "))
	if (deposit_account == 1):
		print("Your checking account balance is $", format(checking_account, "0.2f"), sep='')
		checking_deposit_amount = int(input("How much would you like to deposit? $"))
		checking_account = checking_account + checking_deposit_amount
		print("Your new checking account balance is $", format(checking_account, "0.2f"), sep='')
	elif (deposit_account == 2):
		print("Your savings account balance is $", format(savings_account, "0.2f"), sep='')
		savings_deposit_amount = int(input("How much would you like to deposit? $"))
		savings_account = savings_account + savings_deposit_amount
		print("Your new savvings account balance is $", format(savings_account, "0.2f"), sep='')
	else:
		print("Invalid answer.")
		#print("Withdraw = 1, Deposit = 2, transfer = 3, prediction = 4")
		#user_want = int(input("What would you like to do? ")) 

# Transfer
elif (user_want == 3):
	transfer_account = int(input("What acount would you like to move the money into? Checking = 1 savings = 2 "))
	# From savings to checking
	if (transfer_account == 1): 
		percent = int(input("What percent would you like to transfer? >>> "))
		converted_percent = percent / 100
		amount_moving = savings_account * converted_percent
		savings_account -= amount_moving
		checking_account += amount_moving
		print("Your new checking account balance is $", format(checking_account, "0.2f"), sep='')
		print("Your new savings account balance is $", format(savings_account, "0.2"), sep='')
	# From checking to savings
	elif (transfer_account == 2):
		percent = int(input("What percent would you like to transfer? >>> "))
		converted_percent = percent / 100
		amount_moving = checking_account * converted_percent
		checking_account -= amount_moving
		savings_account += amount_moving
		print("Your new checking account balance is $", format(checking_account, "0.2f"), sep='')
		print("Your new savings account balance is $", format(savings_account, "0.2"), sep='')
	else:
		print("Invalid response please try again.")
		transfer_account = input("checking = 1, savings = 2 ")
		
# Prediction for 6 weeks
elif (user_want == 4):
	total = 0
	number_of_checks = int(input("How many weekly checks would you like to take the adverage of? "))
	for i in range(number_of_checks):
		amount = int(input("What was the amount of the check"))
		total += amount
	adverage = total / number_of_checks
	prediction_account = int(input("What account would you like the prediction for? Checking = 1 savings = 2"))
	if (prediction_account == 1):
		checking_prediction = checking_account + adverage * 6
		print("Your prediction after 6 weeks is $", format(checking_prediction, "0.2f"))
	elif (prediction_account == 2):
		savings_prediction = savings_account + adverage * 6
		print("Your prediction after 6 weeks is $", format(savings_prediction, "0.2f"))
	else:
		print("Invalid response. Please try again.")
		
else:
	print("Invalid response, please try again.")
	#print("Withdraw = 1, Deposit = 2, transfer = 3, prediction = 4")
	#user_want = int(input("What do you want to do?"))
