print("for loop break")

for i in range(14):
    print(i,"power 3 is:",i**3)
    if i == 10:
        break
print("while loop break")
i=1
while True:
    print(i,"power 3 is:",i**3)
    i=i+1
    if(i==10):
        break
    
print("for loop continue")

for i in range(14):
    if i == 10:
        print("10 is skipped")
        continue
    print(i,"power 3 is:",i**3)
    
print("while loop countinue")
j=1
while True:
    if(j == 10):
        print("10 is skipped")
        j =j+1
        continue
    print(i,"power 3 is:",j**3)
    j=j+1
    if(j==14):
        break
