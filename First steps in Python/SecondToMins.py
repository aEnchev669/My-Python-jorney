time_first = int(input())
time_second = int(input())
time_third = int(input())

totalSeconds = time_first + time_second + time_third
mins = int(totalSeconds / 60)
seconds = int(totalSeconds - mins * 60 )

if(seconds < 10):
    print(f"{mins}:0{seconds}")
else:
    print(f"{mins}:{seconds}")