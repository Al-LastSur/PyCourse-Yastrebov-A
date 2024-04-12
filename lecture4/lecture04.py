# def f(x):
#     return x * x

# print (type(f))

# def calc1(a, b):
#     return a+b
# def calc2(a, b):
# #     return a*b
# def math(op, x, y):
#     print (op(x, y))
# # calc1 = lambda a, b: a + b
# # math (calc1, 5, 6)
# math (lambda a, b: a + b, 5, 6)

# task 1. make the list of pairs - an even number and its square
# list2 = [1, 2, 3, 5, 8, 15, 23, 38]
# result = []
# for i in list:
#     if i % 2 == 0:
#         result. append((i, i**2))
# print (result)

# # alternatively with lambda function

# def where (f, col):
#     return [x for x in col if f(x)]

# result = list(map (int, list2))
# print (result)
# result = where (lambda x: x % 2 == 0, result)
# print (result)
# result = map (lambda x: (x, x**2), result)
# print (result)

# list_1 = [x for x in range (1, 21)]
# print (list_1)
# list_1 = list(map (lambda x: x+10, list_1))
# print (list_1)

# task 2. input a row of numbers with separator " " it is takes as a string. 
# change list of string type into int type
# .split(' ')
# data = " 15 12 14 144 18 17 19 "
# print (data)
# # data = data.split()
# # print (data)

# data = list (map(int, data.split()))
# print (data)

# # task3. filter function
# data = [15,147,18,74,985,2145,0,1258]
# res = list (filter(lambda x: x % 10 == 5, data))
# print (res)

# result = list(map (int, res))
# result = filter (lambda x: x % 2 == 0, result)
# result = map (lambda x: (x, x**2), result)
# print (result)

# # task 4. zip function
# result = list(zip ([1,2,3], ["0", "l", "t"], ["д","е","в"]))
# print (result)
# users = ["user1", "user2", "user3", "user4"]
# ids = [4, 5, 9, 14]
# salary = [111,222,333,500]
# data = list (zip(users, ids, salary))
# print (data)

# # task 5. function enumerate
# result = list(enumerate (["Kazan","Smolensk","Rybki", "Chicago"]))
# print (result)

# WORK WITH FILES 
# regimes
# a - to open or create a file (in case if there is none)
# r - read - read a file
# w - open and write to the file (rewrites the file entirely if used twise at the same file)
# w+ - open for writing and reading from it (creates a new file if there is none)
# r+ - open for reading and adding to it new info (creates a new file if there is none)
# open create and write 
colors = ["red", "green", "blue"]
data = open ("file.txt", "a", encoding="utf-8")
data.writelines(colors)
data.close()
# write / rewrite
with open ("file.txt", "w") as data:
    data.write("line 1\n")
    data.write("line 2\n")
# reading only - takes from a file and inputs to console
path = "file.txt"
data = open (path, "r")
for line in data:
    print (line)
data.close()

# os module comands
# os.chdir - change directory
import os
# os.chdor ("c: /Users/...")
# print (os.getcwd()) - print current directory to the console
# print (os.path.basename("file.txt")) - shows the path to the file
# print (os.path.abspath("/Users/...")) - return normalizes absolute name 

# shutil module comands
import shutil
# shutil.copyfile(src, dst) - copy the content of src file to dst file
# shutil.copy (src, dst) - copy content of file to another file or folder
# shutil.rmtree (path) - removes current directory nd all inside directories path shows directory nit a link
