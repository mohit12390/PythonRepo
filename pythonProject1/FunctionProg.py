def greeting(user_name,age,*hobbies):
    print("*"*20)
    print(f"Welcome {user_name} and age is : {age}")
    print(f"Hobbies are ")
    for hobby in hobbies:
        print(f" - {hobby}")
    print("Thanks you for signing in ")
    print ("*"*20)

greeting("Raju",40, "Swimming","Cricket","Hockey","Volleyball")
# greeting("Dinesh",30,"Carrom","Chess","Fighter")
# greeting("Veerapan",40, "TableTennis","Baseball","Boxing")
