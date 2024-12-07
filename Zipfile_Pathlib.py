#CyberStart
#The plot thickens. 
#It seems someone has indeed compromised the company's servers and even set up a new user account named "sshd server". 
#Can you find out what the password is for the account so we can log in and unencrypt the data?
#Tip: The password is the flag.



import zipfile
from pathlib import Path

dataFolder = Path('C:/Users/Public/Documents/CyberStart/Forensics/ForensicsL05C02/')
targetFile= dataFolder/'Hives.zip'
wordFile = dataFolder/'Hwords.txt'

zf = zipfile.ZipFile(targetFile)

with zipfile.ZipFile(targetFile) as file:
    print(file.infolist())
    print(file.namelist())

    with open (wordFile, 'r') as pwdList:	
        for line in pwdList:
            pwrd = str(line)
            try:
                file.extractall(path=targetFile, pwd = bytes(pwrd, 'utf-8'))
                print("\n ++++SUCCESS+++++\n", str(line))
                break
            except:
                print('fail', str(line))