# # Chernika buches
# arr = [5, 8, 6, 4, 9, 2, 7, 3, 12]
# temp = 0
# for i in range(len(arr)-1):
#     sum = arr[i-1]+arr[i]+arr[i+1]
#     if sum > temp:
#         temp = sum
# print(temp)

# Show intersection
# input
var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
# output
# 3 5
var1 = "5 4"
var2 = "1 3 5 7 9"
var3 = "2 3 4 5"

n, m = map(int, var1.split())

set_1 = list(map(int, var2.split()))
set_2 = list(map(int, var3.split()))

intersection = sorted(set(set_1) & set(set_2))

print(*intersection)