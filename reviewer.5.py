age = int(input("Age:   "))
revenue = float(input("Revenue?:    "))
credit = int(input("credit?:    "))
yrs_business = float(input("Business Year?:    "))
has_default = bool(input("Default True/False:   "))
collateral_name = str(input("Name of the item:    "))
collateral_val = float(input("Value of the item:    "))

max_loan = 0
base_fee = 0

if age >= 21 and yrs_business >= 2.0 and has_default == "False":
    print("Eligible <:")
    if credit >= 720: #tier 1
        print("Credit is too High")
        max_loan = 3 * revenue
        if revenue >= 50000: 
            base_fee = max_loan * 0.015
            print("You are hace a lower Income therefore, your fee is:", base_fee)
            if collateral_name >= max_loan:
                print("Collater", collateral_name, "Collater Value", collateral_val, "is Accepted")
            else:
                print("You Have not meet the Requirements in Collateral", collateral_name)
            if 
        elif credit <= 620 and credit < 720: #tier 2
            print("You are meet the Credit Requirements")
            max_loan = 1.5 * revenue
            if yrs_business >= 5:
                base_fee = max_loan * 2
                print("You have low fee:", base_fee)
                if credit < 620: #tier 3
                    print("You have lower credit")
                    if collateral_name >= max_loan:
                        print("Collater", collateral_name, "Collater Value", collateral_val, "is Accepted")
                    else:
                        print("You Have not meet the Requirements in Collateral", collateral_name)
                        
            else:
                base_fee = max_loan * 3.5
                print("You have higher fee", base_fee)
        else:
            base_fee = max_loan * 2.5
            print("You are Have a higher Income", base_fee)
    else: 
        print("Credit is too Low")
else:
    print("You are not Eligible")
