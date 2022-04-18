import requests

import sys
url = "http://api.fixer.io/latest?base="

first_Money = input("first Money:")
second_Money = input("second Money:")
amount = float(input("amount:"))


response = requests.get(url + first_Money)

json_data = response.json()
try:
    print(json_data["rates"][second_Money] * amount)
except KeyError:
    sys.stderr.write("Please enter the correct currencies ")
    sys.stderr.flush()








