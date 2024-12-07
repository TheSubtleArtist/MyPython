#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#


import urllib.request
import urllib.parse

url = "http://127.0.0.1:8082"
values = {'user':'tweetbotuser', 'status-update':'alientest'}
header = {'x-api-key':'tweetbotkeyv1'}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, header)
with urllib.request.urlopen(req) as response:
  the_page = response.read()
  print(the_page)



