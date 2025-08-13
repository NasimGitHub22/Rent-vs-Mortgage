def calculate_repayment_monthly_payment(principal, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = loan_term_years * 12
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)
    return monthly_payment

def calculate_interest_only_monthly_payment(principal, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_payment = (principal * monthly_interest_rate) / 12
    return monthly_payment

# Input for mortgage and renting options
loan_amount = float(input("Enter the loan amount (£): "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
loan_term_years = int(input("Enter the loan term in years: "))
deposit = float(input("Enter the deposit amount (£): "))
sell_price = float(input("Enter the expected selling price of the house (£): "))
sell_years = int(input("Enter after how many years you will sell the house: "))
maintenance_yearly = float(input("Enter the yearly maintenance costs (£): "))
interest_only_period_years = int(input("Enter the interest-only period (in years): "))
appreciation_rate = float(input("Enter the expected annual home appreciation rate (%): "))
rent_monthly = float(input("Enter the monthly rent amount (£): "))
rent_term_years = int(input("Enter the length of tenancy (rent) in years: "))
rent_increase_percentage = float(input("Enter the yearly increase in rent as a percentage: "))

# Repayment Mortgage Calculations
mortgage_payment = calculate_repayment_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
total_paid_to_mortgage = mortgage_payment * sell_years * 12

# Calculate remaining balance for Repayment Mortgage after `sell_years`
remaining_balance = loan_amount
for year in range(sell_years):
    monthly_interest = remaining_balance * (annual_interest_rate / 12 / 100)
    monthly_principal = mortgage_payment - monthly_interest
    remaining_balance -= monthly_principal * 12

equity_from_repayment = deposit + loan_amount - remaining_balance
profit_from_sale_repayment = sell_price - (loan_amount - equity_from_repayment + deposit)

# Interest-Only Mortgage Calculations
interest_only_payment = calculate_interest_only_monthly_payment(loan_amount, annual_interest_rate)
equity_increase_due_to_appreciation = loan_amount * (appreciation_rate / 100) * interest_only_period_years
equity_from_interest_only = deposit + equity_increase_due_to_appreciation
profit_from_sale_interest_only = sell_price - loan_amount + equity_from_interest_only

# Rent Calculations
total_rent_spend = 0
for year in range(rent_term_years):
    total_rent_spend += 12 * rent_monthly
    rent_monthly *= (1 + rent_increase_percentage / 100)

# Display details for Repayment Mortgage:
print("\nRepayment Mortgage Details:")
print(f"Equity Owned: £{equity_from_repayment:.2f}")
print(f"Monthly Mortgage Payment: £{mortgage_payment:.2f}")
print(f"Total Paid to Mortgage: £{total_paid_to_mortgage:.2f}")
print(f"Profit from Sale against Initial Deposit: £{profit_from_sale_repayment:.2f}")

# Display details for Interest-Only Mortgage:
print("\nInterest-Only Mortgage Details:")
print(f"Equity Owned (including appreciation): £{equity_from_interest_only:.2f}")
print(f"Monthly Mortgage Payment: £{interest_only_payment:.2f}")
print(f"Profit from Sale against Initial Deposit: £{profit_from_sale_interest_only:.2f}")

# Display details for Rent:
print("\nRenting Details:")
print(f"Total Spent on Rent over {rent_term_years} years: £{total_rent_spend:.2f}")
