# Let see handling zero division exceptional error
print(5/0)

try:
	print(5/0) except ZeroDivisionError:
	print("you cant divide by zero")

filename="gautam.txt"
try:
	with open(filename) as f:
		content=f.read()
		print(content) except FileNotFoundError:
		print(f"Dear user {filename} may be this file dont exist in directory!")