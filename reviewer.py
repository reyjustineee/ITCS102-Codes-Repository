#input

owner_age = int(input("Enter your age ---> "))
monthly_revenue = float(input("Enter your monthly revenue ---> "))
credit_score = int(input("Enter your credit score ---> "))
years_in_business = float(input("Years in business ---> "))
has_defaults = bool(input("Do you have defaults? (True/False) ---> "))
collateral_name = input("Enter your collateral name ---> ")
collateral_value = float(input("Enter your collateral value ---> "))

#conditions
max_loan = 0
base_fee = 0

if owner_age >=21 and years_in_business >= 2.0 and has_defaults == False:
    print("Baseline Passed")
    if credit_score >= 720: #tier1
        max_loan = monthly_revenue * 3
        print("Maxmimun loanable amount is set to", max_loan)
        print("High Credit Score")
        if monthly_revenue >= 50000:
            print("Revenue higher than 50000")
            base_fee = max_loan * 0.015
            print("Base fee rate is set to", base_fee)
        else:
            print("Revenue lower than 50000")
            base_fee = max_loan * 0.025
            print("Base fee rate is set to", base_fee)

        #collateral
        if collateral_value >= max_loan:
            print("Collaterral", collateral_name, "with a value of", collateral_value, "is ACCEPTED")
        else:
            print("Rejected: Insufficient collateral value for", collateral_name)

        #subcharge
        surge_fee_rate = max_loan * base_fee
        if max_loan % 500!= 0:
            print("Additonal charge added")
            surge_fee_rate += 250
            print("Updated base fee is", base_fee)

    elif credit_score >= 620 and credit_score < 720: #tier2
        print("You have a high credit score")
        max_loan = monthly_revenue * 1.5
        print("Maximum loanable amount is set to", max_loan)
        if years_in_business >= 5.0:
            print("Your business is more than 5 years yay")
            base_fee = max_loan * 0.02
            print("Base fee rate is set to", base_fee)
        else:
            print("Your business is less than 5 years hays")
            base_fee = max_loan * 0.035
            print("Base fee rate is set to", base_fee)

        #collateral
        if collateral_value >= max_loan:
            print("Collaterral", collateral_name, "with a value of", collateral_value, "is ACCEPTED")
        else:
            print("Rejected: Insufficient collateral value for", collateral_name)
        
        #subcharge
        surge_fee_rate = max_loan * base_fee
        if max_loan % 500!= 0:
            print("Additonal charge added")
            surge_fee_rate += 250
            print("Updated base fee is", base_fee)

    elif credit_score < 620: #tier3
        print("\nRejected: Credit score below requirement")
    else:
        print("Invalid")
else:
    print("\nRejected: High Risk Application or Ineligable Owner")