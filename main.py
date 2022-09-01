#link: https://www.youtube.com/watch?v=XKHEtdqhLK8&ab_channel=BroCode

## Loop Control Statements = change a loop execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

#while True: 
    # name = input("Enter your name: ")
    # if name != "": 
        # break

# phone_number = "123-456-7890"
# for i in phone_number: 
    # if i == "-":
        # continue 
    # print(i, end=" ") 

#for i in range(1,21):
    #if i == 13:
        #pass
    #else: 
        #print(i, end=" ")




## nested loop = The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

# rows = int(input("How many rows?: ")) 
# columns = int(input("How many columns?: ")) 
# symbol = input("Enter a symbol to use: ") 
# for i in range(rows): 
#     for j in range(columns):
#         print(symbol,end="")  
#     print() 


## for loop = a statement that will execute it's block of code a limited amount of times
# while loop = unlimited
# for loop = limited 

# for i in range (10): 
#     print(i) 
# for i in range(50,100+1,2): 
#     print(i) 
# for i in "Bro Code": 
#     print(i) 

# import time 

# for seconds in range (10,0,-1):  
#     print(seconds)
#     time.sleep(1) 
# print("Happy New Year!") 


## While loop = a statement that will execute it's block of code, as long as it's condition remains true
# name = ""
# while len(name)==0:
#     name = input("Enter your name: ") 
# print("Hello "+name)

# ## logical operators (and,or,not) = used to check if two or more conditional statements is true
# ##                   (not) = true -> false, false -> true
# temp = int(input("What is the temperature outside?: "))
# if not(temp>=0 and temp <=30): 
#     print("the temperature is good today!")
#     print("go outside!") 
# elif not(temp<0 or temp>30):
#     print("the temperature is bad today") 
#     print("stay inside") 

# ## if statement = a block of code that will execute if its condition is true
# age = int(input("How old are you?: "))

# if age == 100:
#     print("You're a century old.")
# elif age >= 18: 
#     print("Congratulations! You're allowed to drink alcohol.") 
# elif age < 0:
#     print("Sorry! You're not human.")
# else:
#     print("Sorry! You're still a teenager.") 


##slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#    [start:stop:step]    (start,stop,step) 

# name = "Nguyễn Mạnh Cường"
# first_name = name[12:]
# last_name = name[:11]
# print(first_name+" "+last_name)
# print(last_name)
# nickname = name[::3]
# print(nickname)
# reversed_name=name[::-1]
# print(reversed_name)  
#start is inclusive (start at 0)
#stop is exclusive (start at 1)
#step is 1 by default

# website_1 = "http://google.com" 
# website_2 = "http://wikipedia.com"
# slice=slice(7,-4)
# print(website_1[slice])
# print(website_2[slice])


## import math 
# pi=-3.14
# x=1
# y=2 
# z=3 
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x,y,z)) 
# print(min(x,y,z))

# ##user input
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# print("Nice to meet you, "+name+"!")
# print("So you are "+str(age)+" years old. ""I am one year older than you, I am "+str(age+1))
# input("Do you still want to be friend with me? [Type in Yes or No]: ")
# print("Thank you regardless of your answer.")
# height = float(input("And how tall are you?: "))
# print("Now I know you are "+str(height)+" meters, we could be the best match, don't you think?")

##typecasting = convert the data type of a value to another data type
# x=1 #int
# y=2.0 #float
# z="3" #str 

# print("X is "+str(x))
# print("Y is "+str(y))
# print("Z is "+z*3)

## name ="CƯỜNGNGUYỄN"
# print(len(name)) 
# print(name.find("ư"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("G"))
# print(name.replace("C","B"))
# print(name*3)

## multiple_assignment = assign multiple variables at the same time in one line of code
# name="Cường"
# age=21
# attractive=True
# name,age,attractive="Cường",21,True 
# print(name)
# print(age)
# print(attractive)
#Spongebob = 30
#Patrick = 30
#Sandy = 30
#Squidward = 30
# Spongebob=Patrick=Sandy=Squidward=30
# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)
# who,what,when,where,how="Bà Bích","Giỗ","Saturday","Nhà tui","Tự làm"
# print(who)
# print(what)
# print(when)
# print(where)
# print(how)
# Liễu=long=lung=linh="người bên nội bà...i"
# print(Liễu)
# print(long)
# print(lung)
# print(linh)
# variable = a container for a value. Behaves as the value that it contains

## string (a series of characters)
#print("Hello "+name)
#print(type(name))
# first_name = "Nguyễn Mạnh"
# last_name = "Cường"
# full_name = first_name + " " + last_name 
# print("Hello "+full_name)

# #int (integer) (a whole number)
# age = 22
# # age = age + 1
# #or
# age += 1  
# #print(age)
# # print(type(age))
# print("Your age is "+str(age))

# # float = floating point number (a decimal number)
# height = 250.5 
# print (height)
# print(type(height))
# print("Your height is: "+str(height)+" cm")

# #boolean (True of False)
# human = True 
# #print(human)
# #print(type(human))
# print("Are you a human? - "+ str(human))

