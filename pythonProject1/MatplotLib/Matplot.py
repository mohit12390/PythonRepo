import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("Data.csv")
print(data)

emp_count = data.designation.value_counts()
print(emp_count)

plt.bar(emp_count.index, emp_count.values)
plt.xlabel('Designation')
plt.ylabel('No. of Users')
plt.title("Employee VS Designation")
plt.show()