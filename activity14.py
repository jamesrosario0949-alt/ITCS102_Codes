age = int(input("input your age----->:    "))
is_employed = bool(input("is it employed True/blank F ---->   "))
credit_score = int(input("input your credit score--->   "))
annual_income = float(input("input your anual income---->   "))
has_collateral = bool(input("colatteral True/blank F---->  "))
base_rate = 0.0

if age >= 21 and is_employed == True:
    print("eligible to our conditions")
    if credit_score >= 750:
      print("you have a high Credit")
      if annual_income >= 100000:
        base_rate = 4.5
        print("loyalty discount rate:", base_rate)
      else:
        print("You base interest rate:", base_rate)
    elif 600 <= credit_score < 750:
       print("Fair Credit")
       if has_collateral == True:
         base_rate = 7.0
         print("Base rate", base_rate)
    elif annual_income < 40000:
       base_rate = 9.5
       print("base rate", base_rate)
    else:
       base_rate = 8.0
       print("base rate", base_rate)
elif credit_score < 600:
   print("Low Credit. Therefore, you are rejected!")
else:
   print("invalid")
