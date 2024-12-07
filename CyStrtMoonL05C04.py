#
# Write a script to generate a passphrase by taking words from
# /tmp/words.txt
# The wordNumbers array holds three random numbers. Each number
# corresponds to a word in words.txt. So for example
# wordNumbers[1] is the second word in /tmp/words.txt.
# Put a space between each word and print it out
#

passphrase = ''
with open("/tmp/randomwordsnumbers.txt", "r") as nums:
    data = nums.read()

wordNumbers = data.rstrip().split("\n")
#print(wordNumbers)

for i in range(len(wordNumbers)):
  wordNumbers[i] = int(wordNumbers[i])
#print(wordNumbers)

with open("/tmp/words.txt", "r") as words:
  bigList = words.read()
  
wordList = bigList.rstrip().split("\n")
#print(wordList)

for x in range(len(wordNumbers)):
  position = wordNumbers[x]
  passphrase = passphrase + wordList[position] + ' '
 
print(passphrase)
