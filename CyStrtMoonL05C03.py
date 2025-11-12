#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search


import zipfile

dest = '/tmp/'
fpath = '/tmp/alien-zip-2092.zip'
zf = zipfile.ZipFile(fpath)

with zipfile.ZipFile(fpath) as file:
    print(file.infolist())
    print(file.namelist())
		
    for i in range(100, 1000):
      pwrd = str(i)
      try:
        file.extractall(path=dest, pwd = bytes(pwrd, 'utf-8'))
        print("\n ++++SUCCESS+++++\n", i)
        break
      except:
        print('fail', i)