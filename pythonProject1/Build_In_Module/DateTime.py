from datetime import datetime, timedelta
#full date time come with now()
date_time = datetime.now()
print("Date of Today is " , date_time.date())
print("Time of Today is " , date_time.time())
print("day of the date is ", date_time.day)
print("Month of the date is ", date_time.month)
print("Year of the date is ", date_time.year)

#formatted date come with strftime()
formatted_date = date_time.strftime("%Y/%m/%d")

print(formatted_date)

future_date = date_time +  timedelta(days=2)
print(future_date.strftime('%Y/%m/%d %H:%M:%S'))