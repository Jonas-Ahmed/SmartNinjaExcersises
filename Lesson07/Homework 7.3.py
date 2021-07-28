import json
from urllib.request import urlopen

api_key = "d5e958ae63b4fefbe51a413becfe6990"

response = urlopen("http://api.exchangeratesapi.io/v1/latest?access_key=" + api_key + "&format=1").read()

data = json.loads(response)

print(data)

print("the exchange rate from EUR to DKK is " + str(data["rates"]["DKK"]))

print("Can then convert it into a csv file to import into ex. a ERP system")

with open("exchangerate.csv", "w") as exchange:
    exchange.write(str(data))



