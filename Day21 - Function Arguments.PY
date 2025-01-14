def average(a= 12, b=18):
    print("avg iis",(a+b)/2 )

average(10, 2) #here  will run the value given here.
average() #here will run default value given to a,b in function.
average(10) #here will run the value given to a and default value given to b in function.
average(b=10) #here will run the value given to b and default value given to a in function.
average(b=7,a=4) #here keyword argument used. here order does not matter.

def average1(a, b=18):
    print("avg iis",(a+b)/2 )
average1(10)#here giving value of a is Required Arguments

def average2(*numbers): #tuple as input
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("avg is",sum/len(numbers))

average2(10, 20, 30, 40, 50) #here *numbers is used to take multiple arguments.

def info(**data): #dict as input
    print(type(data))
    print("hello", data["fullname"], "your id is",data["id"])

info(fullname = "Ajay", id = 101) #here **data is used to take multiple keyword arguments.


#using return statement
def average(a= 12, b=18):
    return (a+b)/2 

c = average(10, 2)
print(c)