Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")



w= float(weight)

h= float(height)

BMI= w/(h**2)

int_BMI= int(BMI)

print (int_BMI)