"""
This week we will work with dictionaries.
Create a program that includes a dictionary of stocks.
Your dictionary should include at least 10 ticker symbols.
The key should be the stock ticker symbol and the value should be the current price of the stock (the values can be fictional).
Ask the user to enter a ticker symbol.
Your program will search the dictionary for the ticker symbol and then print the ticker symbol and the stock price.
If the ticker symbol isn’t located print a message indicating that the ticker symbol wasn’t found.

"""
flag = True

stocks = {'PLTR': 23.50,
          'GM': 58.57,
          'BABA': 161.52,
          'CCL': 23.83,
          'AMD': 105.60,
          'MIC': 3.71,
          'CLOV': 7.85,
          'XOM': 62.18,
          'CRBU': 19.16,
          'CCXI': 38.41,
          'AAPL': 142.90,
          'TSLA': 785.49,
          'AMZN': 3288.62}

while flag:
	# Get User Input
	for key in stocks:
		print(key, end="  ")

	inputTicker = str(input(f"\nWhich ticker would you like to see?")).upper()

	if inputTicker in stocks:
		print(f"\n The current price of {inputTicker} is ${format(stocks.get(inputTicker), ',.2f')}\n")
	else:
		print("Symbol not found.")

	repeat = input("Would you like to try again? \t 'Y' or 'N'")
	repeat = repeat.upper()
	if repeat != 'Y':
		flag = False
		print("Goodbye")
