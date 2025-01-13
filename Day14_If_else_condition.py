marks = int(input("Enter your Marks:"))

if marks >= 60:
    print("you have passsed the exam")
else:
    print("you failed the exam ")

# elif

if marks == 100:
    print("you have scored full marks so your grade is A  And you will get 50% scholarship")
elif marks >= 95:
    print("you have scored more than 95 your grade is A and  you will get 25% scholarship")
elif marks >= 90:
    print("you passed exam and you grade is A")
elif marks >= 80:
    print("you passed exam and you grade is B")
elif marks >= 70:
    print("you passed exam and you grade is C")
elif marks >= 60:
    print("you passed exam and you grade is D")
else:
    
    attempt = int(input("you failed the exam, how many time have you attempted for the exam: "))
    if attempt >= 3:
        print("you have attempted 3 times so you are not eligible for the exam")
    if attempt == 3:
        print("you have attempted 3 times so you are not eligible for the exam")
    else:
        print("thats not possible to attempt exam more than 3 times")