question = ["1. International Literacy Day is observed on","2. The language of Lakshadweep, a Union Territory of India, is","3. In which group of places the Kumbha Mela is held every twelve years?","4. Bahubali festival is related to","5. Which day is observed as the World Standards Day?","6. Which of the following was the theme of the World Red Cross and Red Crescent Day?"]
answer = ["A","C","B","D","B","D"]
options = ["A. Sep 8\n,B. Nov 28 \n,C. May 2\n,D. Sep 22\n","A. Tamil\n,B. Hindi\n ,C. Malayalam\n,D. Telugu\n","A. Ujjain, Haridwar, Prayag, Nashik ,\nB. Chittorgarh, Sanchi, Mathura, Puri ,\nC. Chittorgarh, Ujjain, Nashik, Prayag,\nD. Rameswaram, Ujjain, Badrinath, Dwarika","A. Islam,\nB. Hinduism ,\nC. Buddhism,\nD. Jainism","\nA. June 26,\nB. Oct 14 ,\nC. Nov 15,\nD. Oct 10","\nA. Refugee and Red Cross wrong,\nB. Urbanisation, Disaster and Red Cross wrong,\nC. Climate Change and Red Cross wrong,\nD. Dignity for all - focus on Children"]
prize = ["1. Rs.10000","2. Rs.20000","3. Rs.30000","4. Rs.40000","5. Rs.50000","6. Rs.60000"]

def game():
    print("Welcome to the game\n")
    print("Here are the rules\n")
    print("You will be asked 6 questions\n")
    print("You have 4 options for each question\n")
    print("You have to select the correct option\n")
    print("If you select the correct option you will win the prize and move to next question\n")
    print("If you select the wrong option you will lose the game\n")
    print("You can quit the game at any time\n")
    
    for i in range(0,len(question)):
        print("Your question is:",question[i],"\nFor prize money of RS",prize[i],"\nYour options are:",options[i])
        x=str(input("Enter your answer:"))
        if x == 0:
            print("You have quit the game")
            if (i == 0):
                print("You have won nothing")
            else:
                money = prize[i-1]
                print("You have won",money)
            break
        elif x == answer[i]:
            print("Your answer is correct")
        elif x not in ["A", "B", "C", "D","0"]:
            print("Invalid input")
            break
        else:
            print("Your answer is wrong")
            if (i == 0):
                print("You have won nothing")
            else:
                money = prize[i-1]
                print("You have won",money)
            break



game()