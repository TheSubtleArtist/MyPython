"""
Briefing L08 C04
Unlocking the Mothership
Agent, it looks like the aliens' insider back on earth is someone with a good understanding of technology. 
The aliens have left him a very complicated backdoor into the ships control system, but we need your expertise to figure it out and break in. 
If we can do that we think we might be able to set the alien ship to self-destruct!
Write a script which connects to the server controlling the entry to the aliens' tech over TCP ("localhost", 10000) and send some random data. 
We've already tried it and it sends back a bunch of random word codes. There's also a file called backdoor.txt containing some random text. 
Use your script to encrypt a message using that text and the word codes. 
Each word is represented by (paragraph_number, line_number, word_number). 
We think sending the encrypted message back is what will unlock the server and give us access to the alien tech!
The server expects all the words in one transmission. 
The words should be stripped of punctuation and sent over separated by newline characters. (\n)
Tip: Send the encrypted message back to the server to get the flag.

Current Situation:
-The paragraph, line, and word numbers are held in two containers. "cWordsNumbers is a single list of all numbers as integers. 
-There are three lists with separate numbers for paragraphs. lines, and words.
-Current problem: HOw to send the numbers to the server? 
"""
import socket

cWordsStrip = []
tParagraphs = []
tLines = []
tWords =[]
randomData = 'GET'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10000))
s.send(randomData.encode())
cWords = s.recv(1024).decode()
print(cWords)
cWords = cWords.replace('\n', ',')
cWords = cWords.split(',')
for each in cWords:
  i = each.replace(' ','')
  cWordsStrip.append(i)
del cWordsStrip[-1]
print(cWordsStrip)
cWordsNumbers = list(map(int, cWordsStrip))
print(cWordsNumbers)

x = len(cWordsNumbers)
print(x)

tParagraphs = cWordsNumbers[0::3]
tLines = cWordsNumbers[1::3]
tWords =cWordsNumbers[2::3]


print(tParagraphs)
print(tLines)
print(tWords)

       
       