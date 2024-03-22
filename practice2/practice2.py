# # Task 1.
# n = 5
# index = 1
# result = index
# while (index <= n):
#     result = result * index
#     index = index + 1
# print (result)

# Task 2.

# A = int(input(">>> " ))
# temp = 0
# n1 = 1
# n2 = 1
# counter = 2
# while temp <= A:
#     temp = n1 + n2
#     n1 = n2
#     n2 = temp
#     counter += 1
#     if temp > A:
#         counter = 0
# if counter != 0:
#     print ("F", counter)
# else:
#     print ("-1")

number = int(input(">>>" ))
fibonacci = 0
f0 = 0
f1 = 1
i = 2
if number == 0:
    print ("F", 1)
elif number == 1:
    print ("F 1 or 2")
else:              
    while number > fibonacci:
        fibonacci = f1 + f0
        f0 = f1
        f1 = fibonacci
        i += 1
if number == fibonacci:
    print (number , i)
else:
    print ("-1")
