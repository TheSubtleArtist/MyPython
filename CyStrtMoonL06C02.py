#
# Hide text in the image /tmp/image.gif
# Append the word alieneye to end of the file.
#
message = 'alieneye'

with open('/tmp/image.gif', 'ab') as f:
  f.write(message.encode('utf8'))