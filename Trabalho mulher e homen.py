num1 = float(input("Please, could you put your hight: "))
man = (72.7*num1) -58
woman = (62.1*num1)-44.7
asnwer = input("Are you a woman or a man: ")
if asnwer == "man":
    print("Your casual status is " + str(man))
else: 
    print("I'll assume your a woman and your status is: " + str(woman))

