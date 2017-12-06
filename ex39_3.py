days ={
'Mo': 'Monday',
'Tue': 'Tuesday',
'Wed': 'Wednesday',
'Thu': 'Thursday',
'Fri': 'Friday'
}

# add days
days['Sat'] = 'Saturday'
days['Sun'] = 'Sunday'

for abbrev, day in list(days.items()):
    print(f' Here is  {abbrev} :  {day}')

count_days = {
'Monday': 1,
'Tuesday': 2,
'Wednesday': 3,
'Thursday': 4,
'Friday': 5,
'Saturday': 6,
'Sunday': 7
}

print(f'The second day in a weekend is {days["Tue"]}')
print(f'Tuesday is the number {count_days[days["Tue"]]} in a week')
