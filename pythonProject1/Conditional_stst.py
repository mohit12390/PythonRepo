# Num1 = int(input("Enter an number to check whether its even/odd - "))
#
# if Num1 % 2 == 0:
#     print(f"{Num1} is even")
# else:
#     print(f"{Num1} is odd")

# users = ['mohit','rajan','deepak']
# if 'mohit' in users:
#     print("user is found in the list ")
# else:
#     print("user is not found in the list ")

age = int(input("Enter an age check whether you are eligible for vote or not !! "))

IsVoterID = False

if age >= 18:
    if IsVoterID:
        print("yes you can vote !!")
    else:
        print("Please apply the Voter ID first ")

else:
    print("You are not eligible for vote !! ")
