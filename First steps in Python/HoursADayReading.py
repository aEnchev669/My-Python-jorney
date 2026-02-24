pagesCount = int(input())
pagesPerHour = int(input())
daysCount = int(input())

hoursNeededPerDay = int((pagesCount / pagesPerHour) / daysCount)

print(f"{hoursNeededPerDay} hours per day")

