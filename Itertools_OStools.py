import itertools
import os

binFilename = "./prgm"
alphabet = 'passwordPASSWORD@$0'

for c in itertools.product(alphabet):
    password = ''.join(c)
    try:
        os.system('./prgm '+ password)
    except:
        print('nope')

# If no password was found by the end, let us know!
print('Password not found.')