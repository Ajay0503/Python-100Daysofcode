l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7)
print(l)
l.insert(2, 100) #at index 2 100 is inserted
print(l)
l.reverse()
print(l)
l.sort(reverse=True)
print(l)
l.sort()
print(l)
print(l.count(1)) #how many time 1 is there
print(l.index(45)) #index of 45
l.remove(45)
print(l)
m=l.copy()
print(m)
k=[533,42,112,44]
c=l+k
print(c)
print(l.extend(k))  #new liist is not created 
print(l)

