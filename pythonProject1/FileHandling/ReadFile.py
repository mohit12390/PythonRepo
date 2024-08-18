with open("User_info.txt",'r') as file:
    content = file.readlines()
    for text in content:
        print("Welcome" , text.rstrip())