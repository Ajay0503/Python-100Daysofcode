a ="!!!!                             Ajay  !! !!!!! Ajay"
b="   Ajay Shanker     "
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.strip())
print(a.rstrip("!"))
print(a.replace("Ajay","AJAY"))
print(a.split(" "))
c= "hi i am aJay"
print(c.capitalize())
print(len(c))
print(len(c.center(50)))
print(a.count("Ajay"))
print(a.endswith("!!!")) #false 
print(a.endswith("Ajay")) #true
str = "Welcome to the Console"
print(str.endswith("to",3,9))
print(a.find("Ajay")) #return first occurence of Ajay in a
print(str.isalnum()) #true if contains only alphabets and numbers
print(str.isalpha()) #true is contain alphabets only fasle as there is space
tr="asdfghjhtrerthj"
print(tr.isalpha())
s = "as gff eew"
print(s.islower())
print(s.isprintable())
f= "                "
print(f.isspace())#is only space

str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str4 = "To Kill The"
print(str4.istitle()) 

str3 = "Python is a Interpreted Language"
print(str3.startswith("Python"))
print(str3.startswith("ytho"))

print(str3.swapcase()) #small becomes capital and vice versa

print(str3.title())

