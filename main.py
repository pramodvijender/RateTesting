import requests

# The End Point that I want to test
url = "http://www.activebanking.macquarie.com"

# A GET request to the API
response = requests.get(url)

# Print the response
response_text = response.text
print(response_text)

# Print the status
print(response.status_code)