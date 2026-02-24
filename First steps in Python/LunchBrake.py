import math

nameOfSeries = input()
episodeLength = int(input())
breakLength = int(input())

if episodeLength >= 10 and breakLength >= 10 and len(nameOfSeries) > 0:
    lunchLength = breakLength / 8
    restTime = breakLength / 4

    freeTime = breakLength - (lunchLength + restTime)
    if freeTime >= episodeLength:
        print(
            f"You have enough time to watch {nameOfSeries} and left with {math.ceil(freeTime - episodeLength)} minutes free time.")
    else:
        print(
            f"You don't have enough time to watch {nameOfSeries}, you need {math.ceil(episodeLength - freeTime)} more minutes.")
