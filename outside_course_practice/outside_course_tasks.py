# Chernika buches
arr = [5, 8, 6, 4, 9, 2, 7, 3, 12]
temp = 0
for i in range(len(arr)-1):
    sum = arr[i-1]+arr[i]+arr[i+1]
    if sum > temp:
        temp = sum
print(temp)
            

 
    