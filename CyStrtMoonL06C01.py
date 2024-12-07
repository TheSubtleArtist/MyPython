import os
for dirpath, dirs, files in os.walk('/tmp/aliendir/'):
	print (files)