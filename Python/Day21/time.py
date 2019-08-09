def angle(h, m):

    if (h < 0 or m < 0 or h > 12 or m > 60):
        print('Wrong input')

    if (h == 12):
        h = 0
    if (m == 60):
        m = 0

    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    angle = abs(hour_angle - minute_angle)

    angle = min(360 - angle, angle)

    return angle


h = int(input('Enter Hour: '))
m = int(input('Enter Minute: '))
if angle(h, m) != 0:
    print('Angle ', angle(h, m))
else:
    print('Overlapping')

# This code is contributed by Danish Raza
