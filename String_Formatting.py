"""
Given an integer, n, print the following values for each integer i from 1 to n :
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

#Numbers
print('{:d}'.format(42)) #formats to decimal
print('{:4d}'.format(42)) #formats to decimal with four padding spaces, right justify
print('{:f}'.format(42)) #formats to float
print('{:06.2f}'.format(3.141592653589793)) #'0' is the padding character, total 6 space, 2 spaces after the
print('{:+d}'.format(42)) #forces the sign
print('{: d}'.format(-42)) #leading space before the negative number
print('{: d}'.format(42)) #leading space aligns
print('{:=5d}'.format(42)) #leading space aligns
print('{:=+5d}'.format(42)) #'=' controls the position of the '+' sign over 5 spaces

"""

def print_formatted(number):
	for i in range(1, n+1):
		# 0 represents the index indicating which format arguement should be placed in that spot
		# width indicates the padding spaced between two rows
		# width is set to be the length of the binary string, that will always have the most characters
		# d, o, X and b converts the string in to decimal, octal, hex, and binary formats repectively
		# Capital X prints the hex characters in upper case
		print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=len("{0:b}".format(n))))  

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



