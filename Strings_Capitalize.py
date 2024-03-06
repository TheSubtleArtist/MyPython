"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
 For example, alison heck should be capitalised correctly as Alison Heck.


"""

if __name__ == '__main__':
	# first tried .title() but that capitalizes the first letter in every space-separated element.
	# for this instance, it string.capitalize() that is needed
	print(' '.join(word.capitalize() for word in input().split()))