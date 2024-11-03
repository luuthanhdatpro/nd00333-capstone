import urllib.request
import json
import os

data =  {
  "data": [
    {
      "age": 25.0,
      "anaemia": 0,
      "creatinine_phosphokinase": 0,
      "diabetes": 1,
      "ejection_fraction": 0,
      "high_blood_pressure": 1,
      "platelets": 0.0,
      "serum_creatinine": 0.0,
      "serum_sodium": 0,
      "sex": 1,
      "smoking": 1,
      "time": 0
    }
  ]
}

body = str.encode(json.dumps(data))

url = 'http://6109292e-50b5-4b0c-b85d-ceaf7da2628c.southcentralus.azurecontainer.io/score'


headers = {'Content-Type':'application/json'}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    print(response)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))