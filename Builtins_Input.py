"""
You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) = k.

The first line contains the space separated values of x and k.
The second line contains the polynomial .

Sample Input

1 4
x**3 + x**2 + x + 1



"""

x, k = map(int, input().split())
if eval(input()) == k:
    print('True')
else:
    print('False')