def fun1():
    try:
     l = [1,2,5,2,4,3,4,5,4,3,3,54]
     i = int(input("enter a number"))
     print(l[i])
    
    except:
     print("some error")
    
    finally:
     print("i am always executed")

x = fun1()
print(x)