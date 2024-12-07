import urllib.request, urllib.error, urllib.parse

link = "http://www.chiquitooenterprise.com/password"


gCode=urllib.request.urlopen(link)
charset = gCode.info().get_content_charset()
xCode = gCode.read().decode(charset)
print('xCode: ', xCode)
revString = xCode[::-1]
print(revString)

answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = urllib.request.urlopen(answer)
response = response.read()
print(response.decode('utf-8'))

