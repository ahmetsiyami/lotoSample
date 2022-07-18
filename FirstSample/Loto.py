import random


lotoResult = [15,21,34,27]

trueCount = 0
for x in lotoResult:
   if x == random.randint(0,35) :
    trueCount += 1
    print("Doğru sayısı",trueCount)

   elif trueCount == 4 :
    print("kazandınız")
    break

   else : 
    print("kaybettiniz, doğru sayınız:",trueCount)
    break
    