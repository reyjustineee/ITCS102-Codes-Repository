#input

age = int(input("Enter your age ---> "))
is_employed = bool(eval(input("Are you currently employed? (True/False) ---> ")))
credit_score = int(input("Enter your credit score ---> "))
annual_income = float(input("Enter your annual income ---> "))
has_collateral = bool(eval(input("Do you have collateral? (True/False) ---> ")))

#condtions

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("\nApplicant pass baseline requirement")
    if credit_score >= 750: #tier1
        print("\nYou have high credit score")
        if annual_income >= 100000:
            base_rate = 4.5
            print("\nYou have high salary and high credit score, your internal rate is", base_rate)
        else:
            base_rate = 5.0
            print("You have high salary and high credit score, your internal rate is", base_rate)
    elif credit_score >= 600 and credit_score <= 750: #tier2
        if has_collateral == True:
            base_rate = 7.0
            print("\nYou have high salary and high credit score, your internal rate is", base_rate)
        elif annual_income <= 40000:
            print("\nYou have Low Salary and Fair Credit Score")
            base_rate = 9.5
            print("\nYou have high salary and high credit score, your internal rate is", base_rate)
        else:
            print("\nFair Credit Score  with No Collateral")
            base_rate = 8.0
            print("\nYou have high salary and high credit score, your internal rate is", base_rate)
    elif credit_score < 600: #tier3
        print("\nRejected: Credit score too low")
    
    else:
        print("\nFailed")

else:
    print("\nRejected: Fails baseline criteria\n")