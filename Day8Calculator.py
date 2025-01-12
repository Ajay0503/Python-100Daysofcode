n = input("Enter 1st number: \t")
m = input("Enter 2nd number: \t")
x = input("Enter the operation you want to perform, \n if 1 the + \n if 2 the - \n if 3 the * \n if 4 the / \n if 5 THEN POWER to a number: \t")
if x == "1":
    print(int(n)+int(m))
if x == "2":
    print(int(n)-int(m))
if x == "3":
    print(int(n)*int(m))
if x == "4":
    print(int(n)/int(m))
if x == "5":
    print(int(n)**int(m))