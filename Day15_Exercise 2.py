import time
Time = time.strftime('%H:%M:%S')

H = int(time.strftime('%H'))

M = int(time.strftime('%M'))

S = int(time.strftime('%S'))


if H < 12:
    print("Good Morning time, is ",Time)
elif H < 18:
    print("Good Afternoon, time is ",Time)
else:
    print("Good Night time, is ",Time)
