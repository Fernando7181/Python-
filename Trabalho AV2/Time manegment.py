def calculator():
 n1 = int(input("Please, input the first two numbers for the time: "))
 if n1 == float:
       print("Please, it has to be a whole number.")
 n2 = int(input("Inset the second number of the time: "))
 if n2 > 60:
      print("Error")
 if n1 > 12:
       print(f'{n1 - 12}:{n2}' +  "pm")
 elif n1 < 12:
            print(f'{n1}:{n2}' + "am")    
 continuee = int(input("Do you wish to continue? 1 for yes\n 2 for no: "))
 while continuee == 1:
     calculator()
     if continuee >= 2:
         break
calculator()
