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

# # add the item to the necessary posiution of the list
# list_5 = [12, 7, -1, 21, 0]
# print (list_5.insert(2, 11)) #first is the position second is the value
# print (list_5) # [12, 7, 11, -1, 21, 0]

# # how to adress the items in a list (we never take the last states element into the list)
# list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print (list_6[0])                   # 1
# print (list_6[1])                   # 2
# print (list_6[len(list_6)-1])       # 10
# print (list_6[-5])                  # 6
# print (list_6[:])                   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print (list_6[:2])                  # [1, 2]
# print (list_6[len(list_6)-2:])      # [9, 10]
# print (list_6[2:9])                 # [3, 4, 5, 6, 7, 8, 9]
# print (list_6[6:-18])               # []
# print (list_6[0:len(list_6):6])     # [1, 7] third number is a step
# print (list_6[::6])                 # [1, 7]

# # work with fixed lists (courtage)
# t = () # class typle - doen not change the elements inside of it
# print (type(t))
# t =(1) # class int
# print (type(t))
# t =(1, 2, 3, 5, ) # class typle - кортеж ?
# print (type(t))

# v = [1, 8, 9]
# print (v)
# print (type(v))
# v = tuple(v)
# print (v)
# print (type(v))
# # a =1
# # b = 2
# a, b = 1, 2
# a = b =1
# a,b,c = v
# print (a,b,c)
# t = (1,2,3,4,5,) # t[0] will not work with tuple
# t = [1,2,3,4,5] # but now you can change it
# # print(t[1])
# # for i in t: # to work with all items on the list
# #     print (i)
# # for i in range(0, len(t)): # to work with all items according the index of the element
# #     print (t[i])
# t[0] = 2
# print (t)

# # dictionaries
# d = {} # empty dictionary
# d = dict() # empty dictionary
# d["q"] = "qwerty" # key and meaning
# print (d)
# d["w"] = "werty" # key and meaning
# print (d["q"]) # to print the meaning according the key

# dictionary = {}
# dictionary = {"up" : "вверх","left" : "вправо", "down": "вниз", "right" : "вправо"}
# print (dictionary)
# print (dictionary["left"])
# # key types may differ
# print (dictionary["up"])
# # key types may differ
# dictionary["left"] = "<="
# print(dictionary["left"])
# # print(dictionary["type"]) # key error type
# del dictionary["left"] # to delete the element from dict
# for item in dictionary: # to see the keys and items in the dictionary
#     print ("{}:{}".format(item, dictionary[item]))
# for item in dictionary: # to see the items only
#     print (item)
# print (dictionary.items()) # each element is a courtage
# # for (k, v) in dictionary.items():# to see the items and keys with function
# #     print (k,v)    

# # multitudes 
# colors = { "red", "green", "yellow", "blue"} # u cannot add the same item to the multitude
# print (colors)
# colors.add ("grey") # to add some item into the multitude
# print (colors)
# colors.remove("red") # to remove some item from the multitude if u try remove the same item onnce more - its a mistake
# colors.discard("blue") # not simply remove but check and then remove if it is inside the multitude
# print(colors)
# colors.clear() # to clear all items from the multitude
# print(colors)

# q = set() # set an empty multitude
# a = {1, 2, 3, 5, 8}                          
# b = {2, 5, 8, 13, 21}                           
# # c = a.copy()                                    # {1, 2, 3, 5, 8} 
# # u = a.union(b)                                  # {1, 2, 3, 5, 8, 13, 21} 
# # i = a.intersection(b)                           # {2, 5, 8}
# # dl = a.difference(b)                            # {1, 3}
# # dr = b.difference(a)                            # {13, 21}
# q = a.union(b). difference(a.intersection(b))   # {1, 21, 3, 13} - 1) a.intesection(b) 2) a,union(b) 3) difference between a.union(b) and a.intersection(b)
# print (q)

# # frozen multitudes
# a = {1, 2, 3, 5, 8, 13, 21}
# b = frozenset(a) # u cannot change the frozen one
# print(b)

# list generators = list comprehension
# list_1 = [exp for item iterable] # add exp so many times as iterable
# list_1 = []
# for i in range(1,101):
#     list_1.append(i)
# list_1 = [i for i in range (1,101)] # shorter form of the above cycle
# print (list_1)
# list_1 = [exp for item in terable (if conditional)]
# list_1 = [i for i in range (1,101) if i % 2  == 0]
# print (list_1)
# list_1 = [(i,i) for i in range(1, 101) if i %2 == 0]
# print (list_1)
list_1 = [i * 2 for i in range (10) if i %2 == 0]
print(list_1)

