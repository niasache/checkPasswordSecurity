password = input("Enter the password you want to check: ")

# the list to store checking values for the password
result = {}

# check for the length of the password
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# check if contains number
digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

# check if contains uppercase letter
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

# console output
if all(result):
    print("Strong Password")
else:
    print("Weak Password")
