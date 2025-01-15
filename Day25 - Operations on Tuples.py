tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
temp =list(tuple1)
temp.append(4)
temp.pop(5) #pop according to index
temp[2]=90
num = tuple(temp)
print(num)

countries1 = ('India', 'USA', 'UK', 'Canada')
countries2 = ("Nepal", "Bhutan", "Sri Lanka")
all = countries1 + countries2
print(all)


tuple2 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple2.count(3)
print("hooe many times 3 is there",res)
print("index of 31 is",tuple2.index(31))
print("index of 3 beweent index 3 and 8 is:",tuple2.index(3,3,8))
print("length of tuple is",len(tuple2))
print("max of tuple is",max(tuple2))
print("min of tuple is",min(tuple2))
print("sum of tuple is",sum(tuple2))