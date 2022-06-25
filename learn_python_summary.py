# python summary (run this code in debug mode so you can understand easily)

print("all explaination will explain in comments (green thing in editor)")
# I'm sorry to not using thai language here, too lazy. zzZZZ

print("hello world") # print is function, hello world is data
print("--------------------------------")
# variable

a = "you just print a" # you can put data in variable (in this case, it's A)
print(a) # printing variable
print("--------------------------------")
# comment

# this thing is called comment it's looks green

# in python we use "hashtag" (#) as comment indicator

'''
for extra extra long comment
you can use three quotes instead
'''

# operators

# I will shows how operators will operates like shown

b = 5+2; print(b) # addition
c = 5-2; print(c) # subtraction
d = 5*2; print(d) # multiplication
e = 5/2; print(e) # division
f = 5%2; print(f) # modulation

print("--------------------------------")

# string formatting (flag)

a = "con"

b = "cat"

print(a,b) # concatinate with two strings

print(a+b) # same as above with no space

print("{} {}".format(a,b)) # using format function to concatinate

print(f"{a}{b}") # using shortened format (f-string)
print("--------------------------------")
# data types and way to change it

# in python, we have multiple data types

a = 15.5 # A will becomes floating number
b = int(a) # B as int form of A
c = float(a) # C as floating number of A
d = str(a) # D as string form of A

print(type(a));print(type(b));print(type(c));print(type(d))# showing data types of variables
print("--------------------------------")
# (there is more of this but i am too lazy to explain)

# input/output

print("please type in terminal, anything")
A = input() # recieve data (default data type is string)
print(f"you just type '{A}' as output") # print what you type
print("--------------------------------")
# if/else conditions

print("edit code data in line '69' to see how if/else operates")
A = "yay"

if A == "yay": # "==" refers to "equals to"
    print("wow") # print when it's in conditions
else :  # if it's not in conditions
    print("aww") # prints another
print("--------------------------------")
# while loops

i = 3

while (i != 0): # "!=" refers to "not equals to"
    print("xD") # print when inside loop
    i -= 1 # add more numbers to "i" variable
print("--------------------------------")
### end of everything almost fundamental for me ###

# wants more advance?, request Wr3nch#6330 in discord, thank you teacher.

# or tell me in here https://github.com/Wr3nch-ren/python-mini-guide