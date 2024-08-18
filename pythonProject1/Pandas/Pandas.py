import pandas

data = pandas.read_csv('Data.csv')
print(data)

#print salary column
# print(data.salary)
# print(data.salary.max())
# print(data.salary.min())
# print(data.salary.sum())

# print("Data of emp id 100 is \n ", data[data.emp_id == 100])
#
# print("Max salary of data \n" , data[data.salary == data.salary.max()])

# print data for any single employee id
# data_100 = data[data.emp_id == 100]
# print(data_100)

# print full name
# full_name = data_100.firstname.values[0] + " "+ data_100.lastname.values[0]
# print(full_name)
#
# print(data.salary.tolist())
# update the data
# data.loc[data.emp_id == 101, 'salary'] = 90000
# print(data)

# remove the record for some condition
# index = data.index[data.emp_id == 101]
# print(index)
# data = data.drop(index)
# print(data)

# Sort data in asc or desc order
# data = data.sort_values(by="salary", ascending=False)
#
# print(data)

# add bonus column increase hike by 20%
# data['Bonus'] = data.salary * 20//100
# data['New Salary'] = data.Bonus + data.salary
# print(data)
#
# # drop column
# data = data.drop('Bonus', axis=1)
# print(data)
#
# data.to_csv("emp_Data.csv")

#
# text = pandas.read_csv("emp_Data.csv")
# print(text)
#
# data = data[data.emp_id == 100]
# print(data)