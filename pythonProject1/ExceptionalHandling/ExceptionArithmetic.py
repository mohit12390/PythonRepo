print(10+3)
print(10//3)
try:
    print(10/0)
except Exception as e:
    print(e,type(e))
    print("Division by zero is not allowed here ")
finally:
    print(20/2)