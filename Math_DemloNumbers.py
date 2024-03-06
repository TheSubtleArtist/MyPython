# Triangle Quest 2
# You are given a positive integer N .
# Your task is to print a palindromic triangle of size N.
# More than 2 lines will result in 0 score. Do not leave a blank line also
# Reference: https://mathworld.wolfram.com/DemloNumber.html

for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)