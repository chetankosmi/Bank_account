initial_balance = float(input("Enter your initial balance: ₹"))
deposit_amount = float(input("Enter the deposit amount: ₹"))
balance = initial_balance + deposit_amount
print("Balance after deposit: ₹", balance)
withdraw_amount = float(input("Enter the amount to withdraw: ₹"))
if withdraw_amount > balance:
    print("Insufficient funds! Withdrawal denied.")
else:
    balance -= withdraw_amount
    print("Withdrawal successful.")
print("Final Balance: ₹", balance)
