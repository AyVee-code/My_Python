##### Lecture 14 #####

#1
a = 0
for i in range(10):
    inp = int(input("Enter a number: "))
    a = a + inp
average = sum/10
print("The average is: ",average)

#2
even = 0
odd = 0
for i in range(12,38):
    if i % 2 == 0:
        even = even + 1
    elif i % 2 != 0:
        odd = odd + 1
print("Sum if even numbers is: ",even)
print("Sum of odd numbers is: ",odd)

#3
inp = int(float(input("Enter your number: ")))
for i in range(1,11):
    product = inp *1
    print(f'{inp} x {i} = {product}')

#4
# in if condition print statement is not written properly.
# indentation is not corret in for loop.
# input is not written properly.
# indentation is not correct in else.

##########################################################################################

##### LECTURE 15 #####

#1
line = 5
for i in range(1, line+1):
    for j in range( 1, line-i + 1 ):
        print(' ', end=' ')  
    for k in range( 1, i+1):
        print( "*", end= " ")
    print('\n')

#2
line = 5
for i in range(1, line+1):
    for j in range(1,i+1):
        print(f"{i}",end=' ')
    print('\n')

##########################################################################################

##### LECTURE 17 #####


##########################################################################################

##### LECTURE 19 #####

a = ' Hello world,,,,....!!Bye max""..}} '

#1
print(a[:8])

#2
upper_case = a.upper()
lower_case = a.lower()
print("UpperCase: ",upper_case)
print("LowerCase: ",lower_case)

#3
trim = a.strip()
no_whitespace = a.replace(" ", " ")
print("Removed leading and trailing whitespace: ",trim)
print("Removed whitespace from middle: ",no_whitespace)

#4
string_1 = "Hello"
string_2 = " World"
concate = string_1 + string_2
print(concate)

#5
replace = a.replace("!!Bye"," ")
print(replace)

#6
remove = a[2:6].upper()
final_string = remove + string_2
print(final_string)

##########################################################################################

##### LECTURE 20 #####

#1
# While loop
i = 1
list = []
while i <= 12:
    list.append(i)
    i += 1
    print(list)
    
# For loop
list = []
for i in range(2,13):
    list.append(i)
    i += 1
    print(list)


#2
mlist = [12, 23, 24, 25, 26, 27, 28, 29, 30, 31]
index = 0
while index < len(mlist):
    print(mlist[index])
    index += 1

#3
mlist = [ 12, 28, 29, 30, 31 ]
sum = 0
index = 0
while index < len(mlist):
    sum += mlist[index]
    index += 1
print("Sum is: ",sum)

#4
# myString = "Hello People!! I'm an Artifical Intelligence Designed to detect malware in the system."
# a = myString.split()
# print(a)
# i = 0
# list = []
# while i<5:
#     remove = input("Enter an alphabet: ")
#     list.append(remove)
#     i += 1
    