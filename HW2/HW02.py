# Task 1. Coins to turn 
counter = 0
counterI = 0
counterJ = 0
i = 0

for i in coins:
    counter +=1
print ("amount ", counter)

for i in coins:
    if i == 1:
        counterI += 1
    if i == 0:
        counterJ += 1
print (counterI)

print ("one side", counterI, "other side", counterJ)
if counter == counterI + counterJ:
    if counterI < counterJ:
        print ("turn", counterI)
    elif counterJ < counterI:
        print ("turn", counterJ)




