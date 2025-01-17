s1 ={1,2,5,6}
s2 ={3,6,7}
print(s1.union(s2))
print(s1,s2)
s1.update(s1,s2) #this update orignal s1 
print(s1,s2) 

city ={"tokyo","madrid","berlin"}
city2={"tokyo","seol","delhi"}
city3 = city.union(city2)
print(city3)
city4 = city.intersection(city2)
print(city4)
city.intersection_update(city2) #this update the orignal city set
print(city)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
cities.difference_update(cities2) #update orignal cities
print(cities)

cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities4.isdisjoint(cities2))
print(cities4.issuperset(cities2))
cities4.add("panipat")
cities4.remove("Berlin") # if berlin not present it give warning if we use discad it will not give warning

#pop delete last element
#delete remove full set
#clear