# -*- coding: utf-8 -*-
"""
Title: Exp1_Part2
Roll No.16010320038
input: lenght, width, height
output: volume, diagonal lenght
"""
import math

#%% Inputs

#this is nesting of functions:
l=int(input("Enter lenght:"))
w=int(input("Enter width:"))
h=int(input("Enter height:"))

#%% Processing
v=int(l*w*h)
dl=int(math.sqrt((l*l)+(w**2)+pow(w,2)))

#%% Output_1

#printing the value
print("\nVolume:",v)
print("Diagonal lenght:",dl)

#%% Output_2
print("\nVolume:{}, Diagonal lenght:{}".format(v,dl))

#Testing
print("hello")




"""
Title: Exp1_Part2
Roll No.16010320038
input: "Just do it!"
"""
#%% 1
x="Just do it!"
print(x)
print(len(x))

#%% 2
print(x[-1])
print(x[len(x)-1])

#%% 3
print(x[5:7])

#%% 4
print(x[7:])

#%% 5
print(x[:5])

#%% 6
y=x[5:].replace('do',"don't do")
print(x[0:5]+y)

#%% lower, upper,split, replace
print(x.upper())
print(x.lower())
print(x.split(' '))
print(x.replace('t','z'))
