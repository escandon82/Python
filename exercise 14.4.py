# Sort JSON keys in and write them into a file

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
with open ("sampleJson.json","w") as write_file:
	json.dump(sampleJson,write_file,indent=4,sort_keys=True)
 
print("Done writing data into Json file")