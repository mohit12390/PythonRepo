
content = ''
try:
    with open("mohit.txt","r") as file:
        content  = file.read()
except FileNotFoundError:
    print('File is not available ')
else:
    print(content)

print('Rest of the code excepted ')