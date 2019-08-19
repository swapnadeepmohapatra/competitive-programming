dist = int(input('Enter the distance in meter: '))
time_hr = int(input('Enter the time in hour: '))
time_min = int(input('Enter the time in minute: '))
time_sec = int(input('Enter the time in sec: '))

total_time_sec = (time_hr * 3600)+(time_min * 60)+(time_sec)

speed = (dist/1000) / (time_sec/3600)
mph = speed / 1.609
print('Your speed in miles/hour: ', mph)
