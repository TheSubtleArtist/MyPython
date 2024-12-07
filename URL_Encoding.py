import pip._vendor.requests as r
import base64

url1 = 'https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D' 
url2 = 'https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
url3 = 'https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
url4 = 'https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
url5 = 'https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
valid = 'https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string='
valid1 = 'https://roambarcelona.com/get-flag?verify=Na2Q%2B'
valid2 = '==&string=<clock pts>'


str1 = r.get(url1)
str2 = r.get(url2)
str3 = r.get(url3)
str4 = r.get(url4)
str5 = r.get(url5)
print(str1.text, str2.text, str3.text, str4.text ,str5.text)

str6 = str1.text + str2.text + str3.text + str4.text + str5.text 
print(str6)

str7 = str6.encode("UTF=8")
print(str7)
str8 = base64.b64encode(str7)
print(str8)
str9 = str8.decode("UTF-8")
print(str9)

str10 = valid + str6
print(str10)
str11 = r.get(str10)
print(str11.text)