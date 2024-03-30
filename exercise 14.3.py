# PrettyPrint following JSON data

sampleJson = {"key1" : "value1", "key2" : "value2", "key3" : "value3"}

PrettyPrintedJson = json.dumps(sampleJson,indent=2,separators=(",","="))

print(PrettyPrintedJson)