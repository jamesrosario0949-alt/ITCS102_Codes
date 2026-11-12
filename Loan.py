loan = float(input("Enter the loan amount: "))
years = float(input("Enter the number of years: "))
months = years * 12
principal = loan / months
print("The monthly principal payment is:", principal)
remaining = loan
print("|Months\t\t|Principal\t\t|Remaining\t\t|Interest\t\t|Monthly Payment\t|")
for x in range(int(1), int(months + 1)):
    remaining -= principal
    interest = remaining * 0.00256
    monthly_payment = principal + interest
    print(f"|{x} months,\t|{round(principal, 2)} principal,\t| {round(remaining, 2)} remaining,\t| {round(interest, 2)} interest, \t|{round(monthly_payment, 2)} monthly payment \t|")