l = [3,4,2,"Ajay",3,4,2,7,5,2]
print(l)
print(type(l))

print(l[0])
print(l[1])
print(l[2])

print(l[-1])

if "Ajay" in l:
    print("Yes")

if 2 in l:
    print("Yes 2")

print(l)
print(l[1:6])
print(l[1:9:2]) #here 2 is step size
print(l[::2]) #here 2 is step size
print(l[::-1]) #reverse the list
print(l[0:])
print(l[:5])

lst =[i*i for i in range(1,11) if i%2==0]
print(lst)
