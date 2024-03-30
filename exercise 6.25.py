# Extract the email service provider name
emaillist=["KSR@datavizion.com","mymail@yahoo.com","milindmali@google.com","snehal@health

for i in emaillist:
	i=i.replace("@",".").split(".")
	print(i[1])