# list_1 = [] # created empy list
# list_1 = list() # alternatively create an empty list with a function 
# list_1 = [1, 2 , 3 ,8]
# print (*list_1)# put starto not show the square pars or commas = to show the values only
# print (len(list_1)) # amount of values inside the list
# for i in list_1:
#     print (i)
# print (list_1[3]) # to print separate element of the list - note the list starts at 0
# print (list_1[-2]) # to start count from the back of list

# list_2 = [1, 5] #
# print (*list_2)
# list_2.append(8) # to add new value to end of list
# print (*list_2)
# list_2.append(18) # to add new value to end of list
# print (*list_2)

# list_3 = []
# print (list_3)
# for i in range(5):
#     list_3.append(i) # add new value to end of list in range between 0 and 4
#     print (list_3)

# # to delete last item from the list
# list_4 = [12, 7, -1, 21, 0]
# print (list_4.pop()) # 0 # to print the last item deleted from the list
# print (list_4) # [12, 7, -1, 21]
# print (list_4.pop()) # 21
# print (list_4) # [12, 7, -1]
# print (list_4.pop()) # -1
# print (list_4) # [12, 7]
# print (list_4.pop(1)) # 7 # delete specific item from the list
# print (list_4) # [12]

# add the item to the necessary posiution of the list
list_5 = [12, 7, -1, 21, 0]
print (list_5.insert(2, 11)) #first is the position second is the value
print (list_5) # [12, 7, 11, -1, 21, 0]
