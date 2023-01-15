 #mortgage loan principal 
loan = float(100000)

 #percent annual interest
Interest_yearly = 0.075
#percent monthly interest
interest_monthly = float(0.075/12)

 # years to pay off mortgage in months(n)
number_months = 30 * 12

#mortgage calculator
numerator = loan * (interest_monthly * (1 + interest_monthly) ** number_months)
denominator = ((1 + interest_monthly) ** number_months) - 1

#amount paid monthly
monthly_repayment = round(numerator / denominator, 2)
print(f"Monthly repayment = ${monthly_repayment}")

#total amount paid after 30 years
Total_paid = round(monthly_repayment * number_months, 2)
print(f"Total amount paid = ${Total_paid}")
