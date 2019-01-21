days_in_month = {
    '1월' : 31,
    '2월' : 28,
    '3월' : 31,
    '4월' : 30,
    '5월' : 31
}

for month, days in days_in_month.items():
    print(month, days)

for month in days_in_month:
    print('{}은 {}일이 있습니다.'.format(month, days_in_month[month]))
