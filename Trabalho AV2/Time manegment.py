n1 = int(input("Please, input the first two numbers for the time: "))
if n1 == float:
    print("Please, it has to be a whole number.")

n2 = input("Inset the second number of the time: ")

if n1 > 12:
    print(f'{n1 - 12}' ":" + n2 +  "pm")
elif n1 < 12:
    print(f'{n1}' ":" + n2 + "am")    
