# Collecting arbitrary number of keyword arguments
def build_profile(fname,lname,**userinfo):
	# build dictionary
	profile={"first Name":fname,"Last Name":lname}
 
	for key,value in userinfo.items():
		profile["key"]=value
 
 	return profile