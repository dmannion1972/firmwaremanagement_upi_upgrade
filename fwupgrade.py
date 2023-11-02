# Import required modules:

import requests           # This module allows for sending various HTTP requests.
import json               # Provides methods to encode and decode data in JSON format.
from pprint import pprint # Enhances the visual presentation of printed data.
from requests.auth import HTTPDigestAuth # Used to authenticate using the HTTP Digest method.
from getpass import getpass             # Facilitates secure input for passwords, without displaying them in the terminal.

# Prompt the user to provide connection and authentication details:

ip_address = input("Enter your IP address: ") # Asks the user for the IP address of the target device.
cam_user = input("Enter username: ")          # Gathers the username needed to access the device.
cam_pass = getpass("Enter password: ")        # Retrieves the password in a secure manner (won't display characters).

# Use the provided credentials to set up HTTP Digest Authentication:
auth = HTTPDigestAuth(cam_user, cam_pass)

# Assemble the request URL by joining the base URL with the user-specified IP address:
url = "http://"+ip_address+"/axis-cgi/firmwaremanagement.cgi"

#payload
payload = {
  "apiVersion": "1.3",
  "context": "abc",
  "method": "upgrade"
}

#files located in same folder
files = {
  'file': [('file.bin',open('Q3538.bin', 'rb'),'application/octet-stream')],
  'payload': json.dumps(payload)
  }


fields={'payload': json.dumps(payload)}

# Dispatch the POST request using the constructed URL, headers, payload, and authentication details:
response = requests.post(url, auth=auth,data=fields,files =[('file',open('Q3538.bin', 'rb'))])

# Display the status code of the response. A 200 code generally means success, while others might indicate errors:
print(response.status_code)

# Output the content of the response in a reader-friendly format for clarity:
pprint(response.text)
