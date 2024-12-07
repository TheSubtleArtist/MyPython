"""
Briefing L08 C01
New Line of Communication
When you were on the last level we discovered the aliens had been communicating with a human insider back on Earth, and by email of all things! 
Well, it seems that may have been a bit of a decoy as they're also exchanging secret encrypted messages from a server on one of the probe ships.
We need you to write a script which can connect over TCP to the following server ("localhost", 10000) and send GET to retrieve the encoded messages, 
then send them back split by \n. We think you'll receive 3 sentences and they're encrypted with a caesar cipher that has a different random offset per sentence.
Tip: Decrypt and send back the sentences to get the flag.

Current Status
-The encryption is a Caesar Shift Cipher
-This Code will return the cipher text
-Each of the three ciphertexts uses a different shift
-All shifts change each time you submit code
-No use of input() is allowed
-Current Problem: How to identify the correct key
"""

import socket

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dMessageList = []
cShifts = [4, 12, 16]

def cDecrypt (encryptedMessage, shift):
    for c in encryptedMessage:
        # find the position in 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord('A')

        # perform the shift
        new_index = (c_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord('A')
        new_character = chr(new_unicode)

        pText =pText + new_character
    return(pText)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10000))
s.send('GET'.encode())
message= s.recv(1024).decode()
print(message)
message = message.upper()
eMessageList = message.split('\n')
print(eMessageList)
eMessageList.pop(0)
eMessageList.pop(-1)
print(eMessageList)

for each in range(len(eMessageList)):
    plnTxt = cDecrypt(eMessageList[each], cShifts[each])
    dMessageList.append(plnTxt)
    dMessageList.append('\n')

print(dMessageList)

for i in range(len(dMessageList)):
    pTxt = dMessageList[i] + '\n'
    s.send(pTxt.encode())