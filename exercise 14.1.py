# Convert the following dictionary into JSON format

import json

data = {"key1" : "value1", "key2" : "value2"} 

jsondata=json.dumps(data) #dict converted to string

print(jsondata)