import argparse
import sys
import math

# Initialize argparser.
parser = argparse.ArgumentParser(description="Loan calculator")

# Add the positional and optional arguments.
parser.add_argument("--type", help="Type of the operation: annuity or diff")
parser.add_argument("--principal", type=int, help="Loan principal")
parser.add_argument("--periods", type=int, help="Months to repay")
parser.add_argument("--payment", type=int, help="Annuity payment")
parser.add_argument("--interest", type=float, help="Rate of interest")

# Parse the args
args = parser.parse_args()
# Namespace(interest=5.6, payment=8722, periods=120, principal=None, type='annuity')

if args.type not in ['annuity', 'diff']:
    print("Incorrect parameters")
    sys.exit()

if args.type == 'diff':
    if args.payment:  # Check if passed payments - is invalid.
        print("Incorrect parameters")
        sys.exit()

# Generate a list of args for checking.
args_list = [args.type, args.principal, args.payment, args.periods, args.interest]

# Check if 4 arguments are passed, quit otherwise.
count = 0
for arg in args_list:
    if arg != None:
        count += 1
if count != 4:
    print("Incorrect parameters")
    sys.exit()

# Check if all numerical types are not None and > 0.
for i in [1,2,3,4]:
    # Convert to float only for comparison.
    if args_list[i] == None:
        pass
    elif float(args_list[i]) < 0.00:
        print("Incorrect parameters")
        sys.exit()

# Calculate number of monthly payments.
if args.type == 'annuity' and (args.principal != None and args.payment != None and args.interest != None):
    principal = args.principal
    monthly_pay = args.payment
    rate = args.interest
    
    rate = rate / (100 * 12)  # Anual tax rate in % converted to monthly float.
    
    log_base = 1 + rate  # Base for the logarithm in number of payments equation.
    months = math.log((monthly_pay/(monthly_pay - rate * principal)), log_base)
    months = math.floor(months) + 1
    overpay = months * monthly_pay - principal
    # Convert months to years and months, print results.
    years = months // 12
    months = months - years * 12
    if not years:
        if months == 1:
            print(f"It will take {months} month to repay this loan!")
        else:
            print(f"It will take {months} months to repay this loan!")
    elif years == 1:
        if months == 0:
            print(f"It will take {years} year to repay this loan!")
        elif months == 1:
            print(f"It will take {years} year and {months} month to repay this loan!")
        else:
            print(f"It will take {years} year and {months} months to repay this loan!")
    elif years > 1:
        if months == 0:
            print(f"It will take {years} years to repay this loan!")
        elif months == 1:
            print(f"It will take {years} years and {months} month to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
    print(f"Overpayment = {overpay}")
    
# Calculate annuity payments.
if args.type == 'annuity' and (args.principal != None and args.periods != None and args.interest != None):
    principal = args.principal
    periods = args.periods
    rate = args.interest
    
    rate = rate / (100 * 12)  # Anual tax rate in % converted to monthly float.
    
    payment = principal * ((rate * ((1 + rate) ** periods) / (((1 + rate) ** periods) - 1)))
    payment = math.ceil(payment)
    overpay = payment * periods - principal
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {overpay}")


# Calculate principal loan amount.
if args.type == 'annuity' and (args.payment != None and args.periods != None and args.interest != None):
    payment = args.payment
    periods = args.periods
    rate = args.interest
    
    rate = rate / (100 * 12)  # Anual tax rate in % converted to monthly float.
    
    # Split equation in denominator in two terms.
    first = rate * ((1 + rate) ** periods)
    second = ((1 + rate) ** periods) - 1
    principal = math.floor(payment / (first / second))
    overpay = periods * payment - principal
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {overpay}")

# Calculate the differentiated monthly payments.
if args.type == 'diff':
    principal = args.principal
    periods = args.periods
    interest = args.interest / (100 * 12) # Anual tax rate in % converted to monthly float.
    total = 0
    # Print each month - Month 1: payment is 65750
    for i in range(1, periods + 1):
        first_term = principal / periods
        second_term = interest * (principal - ((principal * (i - 1)) / periods))
        diff_month = math.ceil(first_term + second_term)
        total += diff_month
        print(f"Month {i}: payment is {diff_month}")
    overpay = total - principal
    print(f"\nOverpayment = {overpay}")