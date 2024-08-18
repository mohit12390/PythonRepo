import random

print("The Dice come on the face is : " ,random.randint(1,6))


fruits = ["Orange","Papaya","Kivi","Grapes","Banana","Apple"]
print("The Fruits I selected is " , random.choice(fruits))

random.shuffle(fruits)

print(fruits)