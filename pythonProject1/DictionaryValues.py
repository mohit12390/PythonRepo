marks = {
        'English' : 80,
        'Hindi': 50,
        'Maths': 40
    }

print(marks)
# type of data type
print(type(marks))
# get key value
print(marks.get('English'))
#get keys and value
print(marks.values())
#update the value of keys
marks['Hindi'] = 100
print(marks)
# delete the Hindi keys
del marks['Hindi']
print(marks)
#length of keys and valyes
print(len(marks))