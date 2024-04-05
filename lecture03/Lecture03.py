# def sumNumbers(n):
#     summa = 0
#     for i in range (1, n+1):
#         summa += i
#     return summa

# a = sumNumbers(5)
# print(a)

# def sum_str(*args): # unlimited number of arguments into function
#     res = ""
#     for i in args:
#         res+= i
#     return res

# print(sum_str("q", "e", "g", "s"))

# import modul1
# print(modul1.max1(5,9))

# alternatively
# from modul1 import max1 from modul1 import * - means import alll functions from modul1
# print(max1(15,9))

# import modul1 as m1 # rename file only inside the rpogram
# print(m1.max1(5,9))

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1,11):
#     list_1.append(fib(i))
# print (list_1)

# #  quick sorting
# def quickSort (array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1: ] if i <= pivot]
#     more = [i for i in array[1: ] if i > pivot]
#     return quickSort(less) + [pivot] + quickSort(more)
    
# print (quickSort([14,5,18,19,22,201]))

#  union sort
def mergeSort(nums):
    if len(nums) > 1:
        mid = len (nums) // 2
        left = nums [:mid]
        right = nums [mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k =0
        while i < len(left) and j < len(right):
            if left [i] < right [j]:
                nums [k] = left [i]
                i+=1
            else:
                nums [k] = right [j]
                j+=1
            k+=1
        while i < len(left):
            nums[k] = left [i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right [j]
            j+=1
            k+=1
            
list1 = [1,2,3,2,1,3,4,5,6,11,534]
mergeSort(list1)
print (list1)