#This is a student loan calculator


# input variables that take in the principle loan from the user and the years the user will have the loan for. Also saves the original principle to be used in the loan function.
print('Welcome to the Student Loan Calculator')
principle = float(input('Enter the amount of the loan in dollars with (no commas):\n'))
original_principle = principle
years = int(input('Enter the number of years the loan will be for:\n'))

# function that calculates loan data and prints the output describing the loan data


def loan_calculations():
    monthly_payment = (principle*interest_rate)/(times_compounded_yearly*(1-(1+(interest_rate/times_compounded_yearly))**(-years*times_compounded_yearly)))
    total_paid_on_loan = monthly_payment * times_compounded_yearly * years
    total_interest_paid = total_paid_on_loan - original_principle
    fee = original_principle * fee_rate
    total_costs_over_principle = fee + total_interest_paid
    print('---------------------------------')
    print(loan_type)
    print('Principle: %d' % original_principle)
    print('Interest Rate:', round(float(interest_rate*100), 2))
    print('Years: %d' % years)
    print('Monthly Payment:', float(round(monthly_payment, 2)))
    print('Total Paid on Loan:', float(round(total_paid_on_loan, 2)))
    print('Total Interest Paid:', float(round(total_interest_paid, 2)))
    print('Additional Fees Paid:', float(round(fee, 2)))
    print('Total Costs over Principle:', float(round(total_costs_over_principle, 2)))

# Subsidized Federal Loans specifications


times_compounded_yearly = 12
fee_rate = 0.01051
interest_rate = 0.034
loan_type = 'Subsidized Federal Direct Loan'
loan_calculations()

# Unsubsidized Federal Direct specifications


times_compounded_yearly = 12
fee_rate = 0.01051
interest_rate = 0.068
principle = principle * (1 + interest_rate * 4.25)
loan_type = 'Unsubsidized Federal Direct Loan'
loan_calculations()

# Federal Plus Loan specifications


principle = original_principle
fee_rate = 0.04204
interest_rate = 0.079
principle = principle * (1 + interest_rate * 4.25)
loan_type = 'Federal Plus Loan'
loan_calculations()
print('---------------------------------')


