import requests
from getpass import getpass
from requests.exceptions import Timeout

response = requests.get("https://www.google.com")

print(response)

print(response.status_code)

print(response.content)

print(response.text)

print("\n                  '''''''''''''''''''''                              ")

print(response.headers, end='\n')

print('\n', response.headers["content-type"])

# rr = response.text
#
# print(rr['headers']['content-type'])

ar = requests.get("https://api.github.com/user", auth=("ScarletMoony", getpass()))

print(ar.json(), end='\n')

try:
    response = requests.get("https://www.google.com", timeout=1)
except Timeout:
    print("Timeouted")

print(response)
