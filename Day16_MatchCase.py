x = int(input("Enter a number: "))

match x:
    case 0:
        print("You entered zero")
    case 1 if x==7:
        print("You entered 7") 
    case _ if x > 5:
        print("you entered number more than 5")
    case _ if x == 5:
        print("you entered number 5")
    case _:
        print ("you enterd number less than 5 but greater than 0")