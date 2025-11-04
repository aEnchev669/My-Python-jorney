lenght = int(input())
width = int(input())
height = int(input())
percents = float(input()) / 100

totalVolume = lenght * width * height
volumeInLiters = totalVolume / 1000
neededLiters = volumeInLiters * (1 - percents)

print(neededLiters)
