# Access the value of key2 from the following JSON

sampleJson ="""{"key1": "value1", "key2": "value2"}"""

data=json.loads(sampleJson) # converted to dictionary

data["key2"]