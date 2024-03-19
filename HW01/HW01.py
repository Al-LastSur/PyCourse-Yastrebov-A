# # Task 1. Find the sum of all digits in three-digit number
# n = int( input ("Input three-digit Number here: ", ))
# result = 0
# while (n > 0):
#     # if (n > 0):
#         result = int(n % 10) + result
#         n = n / 10

# print ("Ther summ of {n} digits is ", result)

# # Task 2. Children make origami birds
# OrigamiBirds = int( input ("Amount of Orighami Birds Made Altogether: ", ))
# temp = OrigamiBirds / 6
# K = int(temp * 4)
# PS = int(temp)
# print (PS , K, PS)

# # #Task 3. Lucky Ticket
# # Ticket = input ("Input Ticket Number(6-digits): ", ) # if input as string
# # FirstHalf = int(Ticket[0]) + int(Ticket[1]) + int(Ticket[2])
# # SecondHalf = int(Ticket[3]) + int(Ticket[4]) + int(Ticket[5])
# # result = FirstHalf - SecondHalf
# # if result == 0:
# #     print ("yes")
# # else:
# #     print ("no")
# # print (result)

# Ticket = int(input("Input Ticket Number(6-digits): ", )) # if input transferred as integer
# FirstHalf = int(Ticket / 1000)
# SecondHalf = int(Ticket % 1000)
# FirstSum = 0
# SecondSum = 0
# print (FirstHalf, SecondHalf)
# while (FirstHalf > 0):
#     FirstSum = FirstSum + int(FirstHalf % 10)
#     FirstHalf = FirstHalf / 10

# while (SecondHalf > 0):
#     SecondSum = SecondSum + int(SecondHalf % 10)
#     SecondHalf = SecondHalf / 10    

# if (FirstSum == SecondSum):
#     print ("yes")
# else:
#     print ("no")
    
# Task 4. Split chocolate bar
print("You have a chocolate bar")
long = int(input("The bar's length is: ", ))
wide = int(input("The bar's width os : ", ))
split = int(input("Can you take pieces with one cut: ", ))
if (split % long == 0 or split % wide == 0):
    print("You can take pieces with one cut")
else:
    print("You can't take pieces with one cut")