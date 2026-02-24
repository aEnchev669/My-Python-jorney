packetsPensCount = int(input())
packetsMarkersCount = int(input())
litreOfCleaningPrep = int(input())
percentDiscount =  int(input())

PACKOFPENPRICE = 5.80
PACKOFMARKERSPRICE = 7.20
LITREOFPREPARATIONPRICE = 1.20

pensPrice = packetsPensCount * PACKOFPENPRICE
markersPrice = packetsMarkersCount * PACKOFMARKERSPRICE
preparationPrice = litreOfCleaningPrep * LITREOFPREPARATIONPRICE

totalPrice = pensPrice + markersPrice + preparationPrice
totalPriceWithDiscount = totalPrice *  (100 - percentDiscount) / 100

print(round(totalPriceWithDiscount,2))