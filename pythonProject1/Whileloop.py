# user_input = ""
# while user_input != 'q':
#     user_input = input("Enter a no. or press q for quit !! - ")
#     if user_input.isdigit():
#         if int(user_input) % 2 == 0:
#             print(f"{user_input} is even")
#         else:
#             print(f"{user_input} is odd")

num = [2,45,2,45,34,67,2]

while 2 in num:
    num.remove(2)


print(num)