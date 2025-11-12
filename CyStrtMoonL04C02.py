


#corrected code

#
# Fix the below script to read from each agent file found in /tmp.
# Example agent profile would be /tmp/agent-1.txt
# The contents of each of the agent files makes up the flag
#


import os.path



for i in range(1, 21):
  fname = "/tmp/agent-" + str(i) + ".txt"  
  if os.path.isfile(fname):
    with open(fname, 'r') as content_file:
        content = content_file.read()
        print(content.strip())
