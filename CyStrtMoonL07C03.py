#
# Setup server listening on ('localhost', 10000)
# receive data then send back XORed with the key
# attackthehumans
#
# If you get an address already in use error then try again in a few
# moments.
#

# Reference for testing actual XOR: 
# https://xor.pw/
# https://www.binaryhexconverter.com/ascii-text-to-binary-converter
# attackthehumans binary: 
# 01100001 01110100 01110100 01100001 01100011 01101011 01110100 01101000 01100101 01101000 01110101 01101101 01100001 01101110 01110011 

# Data: '!V)R>\)'
# Data Binary: '00100001 01010110 00101001 01010010 00111110 01011100 00101001'

# Data / Key XOR Binary: '1100001 01110100 01110100 01100001 01100011 01101011 01110100 01101000 01000100 00111110 01011100 00111111 01011111 00110010 01011010'

# Current Situation: code works, but something never sends the right answer. I don't know where my error is.


from encodings import utf_8
import socket

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a+") as myfile:
    myfile.write(msg + "\n")
    for line in myfile.read():
      print(line)

def doBinary(rInput):
  return(''.join(format(ord(x), '0b') for x in rInput))

def doBinary2(string):
  binList = []
  byteList = bytearray(string, "utf-8")
  for byte in byteList:
    binString = bin(byte)
    binList.append(binString)
  binList = [c.replace('b','') for c in binList]
  bData = ''.join(map(str, binList))
  print(bData)

  return bData



# Add zeroes to the front of a binary string
def addZeros(bsInput, n):
  for x in range(n):
    bsInput = "0" + bsInput
  return bsInput  


# perform XOR specifically when inputs are strings of different lengths
def doXOR (key, data):
  # get lengths of the two inputs
  lenKey = len(key)
  print("lenKey: ", lenKey)
  lenData = len(data)
  print("lenData: ", lenData)
  # Make both strings of equal length
  # Insert 0s at the beginning of the shorter string
  if (lenKey == lenData):
    print('Same Length')
    pass
  elif (lenKey > lenData):
    print("Key is Longer")
    data = addZeros(data, lenKey - lenData)
  elif (lenKey < lenData):
    print("Data is Longer")
    key = addZeros(key, lenData - lenKey)

  result = [ord(a) ^ ord(b) for a,b in zip(key,data)]
  lData = ''.join(map(str, result))
  return(lData)

# Challenge key
ckey = 'attackthehumans'

# Test key
tkey = 'attackthehumans'

# Test data
tdata ='!V)R>\)^'

def testFunctions(tkey, tdata):
  print("tKey: ", tkey)
  print("tData: ", tdata)
  bData = doBinary2(tdata)
  print('length bData: ', len(bData))
  print('bData: ', bData)
  bKey = doBinary2(tkey)
  print('length bKey: ', len(bKey))
  print('bKey: ', bKey)
  print(doXOR(bKey, bData))


testFunctions(tkey, tdata)

"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 10000))
s.listen(1)

conn, addr = s.accept()
rData = conn.recv(1024)
dData = rData.decode('utf-8')
debugMsg(dData)
bData = doBinary(dData)
debugMsg(bData)
debugMsg('x')
bKey = doBinary(ckey)
debugMsg(bKey)
sData = doXOR(bKey, bData)
conn.send(bytes(sData, 'utf-8'))
rcp = conn.recv(1024)
rcpt = rcp.decode('utf-8')
"""