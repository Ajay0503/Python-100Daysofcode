a = [12,43,23,11,44,22,55,22,33,65,98,33]

for index,m in enumerate(a): #givve index and value together
    print(m)
    if(index == 10):
        print("good")
    index += 1

print("another")
for index,m in enumerate(a,start=1): #can change the start of indexing
    print(m)
    if(index == 10):
        print("good")
    index += 1
    