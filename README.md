# Mortgage vs Rent Calculator

This Python script compares the financial outcomes of **buying a property** (via either a repayment mortgage or an interest-only mortgage) versus **renting** over a given period.

It calculates:
- Monthly mortgage payment amounts  
- Total paid over the ownership/rental period  
- Equity owned at the point of sale  
- Profit from selling the property (against the initial deposit)  
- Total cost of renting for the same period  

---

## Features

### 1. Repayment Mortgage
- Monthly repayment amount  
- Total paid towards mortgage until sale  
- Remaining mortgage balance after a chosen number of years  
- Equity owned at the time of sale  
- Profit from sale (compared to initial deposit)  

### 2. Interest-Only Mortgage
- Monthly interest payment amount  
- Equity from appreciation  
- Profit from sale (against initial deposit)  

### 3. Rent
- Total rent paid over tenancy duration  
- Yearly rent increases accounted for  

---

## How to Use

### 1. Install Python
Make sure you have Python 3.11+ installed:  
```bash
python --version
````

### 2. Download the Script

Save the script as `MvR_Calc.py` (or any name you prefer).

### 3. Run the Script

```bash
python MvR_Calc.py
```

### 4. Enter the Required Inputs

You’ll be prompted for:

* Loan amount (£)
* Annual interest rate (%)
* Loan term (years)
* Deposit (£)
* Expected selling price (£)
* Years until sale
* Annual maintenance cost (£)
* Interest-only period (years)
* Expected annual appreciation rate (%)
* Monthly rent (£)
* Tenancy length (years)
* Annual rent increase (%)

### 5. View Results

The script will display:

* **Repayment Mortgage Details**
* **Interest-Only Mortgage Details**
* **Renting Details**

---

## Example Output

```
Repayment Mortgage Details:
Equity Owned: £160,000.00
Monthly Mortgage Payment: £2,300.45
Total Paid to Mortgage: £276,054.00
Profit from Sale against Initial Deposit: £100,000.00

Interest-Only Mortgage Details:
Equity Owned (including appreciation): £120,000.00
Monthly Mortgage Payment: £1,500.00
Profit from Sale against Initial Deposit: £80,000.00

Renting Details:
Total Spent on Rent over 10 years: £300,000.00
```

---

## Notes

* This is a **simplified model** and does not include taxes, insurance, inflation (except rent increase), or early repayment penalties.
* Use for **illustrative purposes only**
If you like, I can also add a **comparison result** section in the README that shows which option was cheapest based on the output of your script. That way the README looks even more complete.
```
