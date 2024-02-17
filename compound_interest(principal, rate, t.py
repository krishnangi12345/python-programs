def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period (in years): "))

print("Compound Interest:", compound_interest(principal, rate, time))
