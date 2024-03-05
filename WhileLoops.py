"""
For this week’s assignment, write a program that uses a while loop to determine how long it takes for an investment to double at a given interest rate.
The input will be an annualized interest rate and the initial investment amount, and
the output is the number of years it takes an investment to double.
"""
flag = True
while flag:

	initialInvestment = float(input('What is your initial investment'))
	annualPercentageRate = float(input('Enter the quoted annual percentage rate')) / 100
	year = 0
	newBalance = initialInvestment

	while newBalance < initialInvestment * 2:
		newBalance = newBalance + (newBalance * annualPercentageRate)
		year += 1

	print(f'It will take {year} years to double an initial investment of ${format(initialInvestment, ",.2f")} \n At the end of {year} years, '
	      f'the balance will be ${format(newBalance, ",.2f")} ')
	repeat = input("Would you like to perform another calculation? \n 'Y' or 'N'")
	if repeat != 'Y':
		flag = False
