
a = 3
b = 5

# def sum (a,b):
#     result = 0
#     if a > 0:
#         result +=1
#         a -= 1
#     return result
# print (sum(5, 3))

def sum (a,b):
    if b >0:
                return sum (a+1, b-1)
    else:
        return a


# while b > 0:
#     a = a + 1
#     b-=1
# print (a)
print (sum (3,15))