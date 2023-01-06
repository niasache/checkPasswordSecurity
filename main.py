password = input("Enter the password you want to check: ")

# the list to store checking values for the password
result = []

# check for the length of the password
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

# check if contains number
digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

# check if contains uppercase letter
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

print(result)
print(all(result))