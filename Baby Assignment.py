# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:40:18 2024

@author: someo
"""

print("Welcome to Assignment-1")

Num1=int(input("Num1="))
Num2=int(input("Num2="))
Add=Num1+Num2
print("Add=",Add)

Weight=float(input("Weight in Kg="))
Height=float(input("Height in Cm="))
BMI=Weight/(Height/100)**2
print("Your BMI Index =",BMI)
print(float(input("Enter the BMI Index=")))
if(BMI<18):
    print("Under Weight")
if(BMI>18.1 and BMI<29.9):
    print("Normal")
if(BMI>30 and BMI<34.9):
    print("Over Weight")
if(BMI>35):
    print("Very Over Weight")