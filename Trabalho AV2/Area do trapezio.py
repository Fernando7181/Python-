import time 

print("Welcome to the Trapezoid Area Calculator :) ")
time.sleep(2)

larger_b = float(input("What's the lenght of the larger side: "))
smaller_b = float(input("Please, input the lenght of the smaller side: "))
height = float(input("And Put the Height of the trapezoid: "))
trapezoid_area = (((larger_b + smaller_b)* height)/2)
print("The Trapezoid Area is " + str(trapezoid_area))