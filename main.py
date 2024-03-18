# #Task 1.
# m = int(input ("Innput distance length:", ))
# n = int(input ("Innput distance travelled per day:", ))
# #n = 700 # distance travelled per day
# #m = 750 # distance length
# result = -(-m // n) # to round up scale
# print(result) # printed result

# #Task 3.
# students1 = int(input("1 form student amount: ", ))
# students2 = int(input("2 form student amount: ", ))
# students3 = int(input("3 form student amount: ", ))
#
# print("Total desks ", int(-(-students1 // 2 )) + int(-(-students2 // 2)) + int(-(-students3 // 2 )))

# Task 5.
actualNo = int(input("The ticket says it's: ", ))
seatedNo = int(input("But actually was: ", ))
result = 0
if seatedNo == actualNo:
    print("We need more info")
else:
    result = seatedNo - 1 + actualNo

print("The train has: ", result, " vagons")