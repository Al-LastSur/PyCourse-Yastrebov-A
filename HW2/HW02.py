# # Task 1. Coins to turn 
# counter = 0
# counterI = 0
# counterJ = 0
# i = 0

# for i in coins:
#     counter +=1
# print ("amount ", counter)

# for i in coins:
#     if i == 1:
#         counterI += 1
#     if i == 0:
#         counterJ += 1
# print (counterI)

# print ("one side", counterI, "other side", counterJ)
# if counter == counterI + counterJ:
#     if counterI < counterJ:
#         print ("turn", counterI)
#     elif counterJ < counterI:
#         print ("turn", counterJ)

# # Task 2. Brother and Sister
# s = int(input("Sum of numbers " ))
# p = int(input("Plex of numbers " ))
# y = 0
# for x in range(1, 1001):
#     y = s - x
#     if y == p / x:
#         print(x, y)
#         break
#     else:
#         x+=1

# Task 3. All numbers of 2 grade
n = 16
for i in range(0, n+1):
    result = 2 ** i
    if i == 0:
        print (1)
    if (result <= n) and (result % 2 == 0 ):   
        print (result)
