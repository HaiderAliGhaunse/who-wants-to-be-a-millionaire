import sys
import random
scoreslist = []
PRIZE = ["£0","£100" , "£200", "£300", "£500", "£1000", "£2000", "£4000", "£8000",
       "£16000", "£32000", "£64000", "£125000", "£250000", "£500000", "£1 Million" ]
class user:
    audienceused = False
    callused = False
    fiftyused = False
    def __init__(self,name):
        self.name = name
        print("Welcome",name,"to who wants to be a millionaire")
    def addscore(self,scoreslist,z):
        scoreslist.append((self.name,PRIZE[z]))
    def audience(self):
        self.audienceused = True
    def call(self):
        self.callused = True
    def fifty(self):
        self.fiftyused = True
        
def intro():
    print("You will be playing who wants to be a millionaire")
def menu():
    print("""Choose betweem these three options
         1 - Start game
         2 - add questions
         3 - Show scores
         4 - exit application
         """)
    choice = int(input("What option do you choose "))
    while choice not in range(1,5) :
        choice = int(input("Your choice was inavalid. What option do you choose "))
    if choice == 1:
        main()
    elif choice == 2:
        questions()
    elif choice == 3:
        scores()
    elif choice == 4:
        sys.exit()
    else:
        menu()
def start_game():
    with open("questions.txt","r") as f:
        line_count = 0
        for line in f:
            if line != "\n":
                line_count += 1
    if line_count < 90:
        print("Sorry you don't have enough questions please add some questions or reset the questions")
        menu()
    z = 0
    x = 0
    y = 0
    name = input("Enter your name ")
    player = user(name)
    while x < 15:
        
        with open("questions.txt","r") as f:
            lines =  f.readlines()
        print("The questions is " + lines[0 + y])
        print("1=" , lines[1 + y], "\t\t", "2=" , lines[2 + y] )
        print("3=" , lines[3 + y], "\t\t"+ "4=" , lines[4 + y] )
        correct = int(lines[5 + y])
        if correct == 1:
            a = lines[1 + y]
        elif correct == 2:
            a = lines[2 + y]
        elif correct == 3:
            a = lines[3 + y]
        elif correct == 4:
            a = lines [4 + y]
        lifelines(correct,lines,y,a,player)
        guess = int(input("enter your guess "))
        if guess not in range (1,5):
            guess = int(input("Invalid guess, try again "))
        if guess == correct:
            PRIZE[z]
            z += 1
            print("That was right you have",PRIZE[z],"points")
            x += 1
            y += 6
        else:
            print("Unlucky",name,"That was wrong you scored",PRIZE[z],"points", "The correct answer was",a)
            player.addscore(scoreslist,z)
            
            leaderboard(scoreslist)
            menu()
    print("Well done",name," you have won who wants to be a millionaire")
    player.addscore(scoreslist,z)
    menu()
def questions():
    print("""    Do you want to
            1 - reset questions
            2 - Add a questions
            3 - delete a question
""")
    option = int(input("Which option do you want "))
    while option not in range(1,4):
        option = int(input("Your option was invalid, which option do you want "))
    if option == 1:
        reset()
    elif option == 2:
        add()
    elif option == 3:
        delete()

def reset():
    
    with open("recover questions.txt","r") as f:
        lines =  f.read()
    with open("questions.txt","w") as f:
        f.write(lines)
    menu()

def add():
    with open("questions.txt","r") as f:
        line_count = 0
        for line in f:
            if line != "\n":
                line_count += 1
    
    if line_count == 90 :
        print("You have 15 questions if you want to add more you need to delete questions")
        menu()
    else:
        f = open("questions.txt","a")
        question =input("What is your question ")
        choice1 =input("input what your first choice is ")
        choice2 =input("input what your second choice is ")
        choice3 =input("input what your third choice is ")
        choice4 =input("input what your fourth choice is ")
        answer  =input("which choice is right?(1-4) ")
        f.write("\n" + question)
        f.write("\n" + choice1)
        f.write("\n" + choice2)
        f.write("\n" + choice3)
        f.write("\n" + choice4)
        f.write("\n" + answer)
                
        f.close()
        f = open("questions.txt","r")
        print(f.read())
        f.close

def delete():
    y = 0
    x = 1
    with open("questions.txt","r") as f:
        lines = f.readlines()

    while y < 86:
        print(x,lines[0+y])
        y += 6
        x += 1
    removed = int(input("Which question do you want removed "))
    deleted = (removed -1)*6
    del lines[deleted]
    del lines[deleted]
    del lines[deleted]
    del lines[deleted]
    del lines[deleted]
    del lines[deleted]

    with open("questions.txt","w+") as f:
        for line in lines:
            f.write(line)

    menu()

def scores():
    choice = int(input("""Do you want the scores to be listed alphabetically or ordered by prize
                         1 = Alphabetically
                         2 = ordered by prize amount
                   """))
    while choice not in range(1,3):
         choice = input("Please choose 1 or 2 ")

    if choice == 1:
        sorted_alpha = sorted(scoreslist, key=lambda tup: tup[0])
        print(sorted_alpha)
    elif choice == 2:
        
        sorted_by_money = sorted(scoreslist, key=lambda tup: tup[1], reverse =True)
        print(sorted_by_money)
    menu()
def leaderboard(scoreslist):
    pass

def lifelines(correct,lines,y,a,player):
    choice = input("Do you want a lifeline (y/n) ")
    while choice != "y" and choice != "n":
        choice = input("Please choose (y/n) ")
        
    if choice == "y":
        lifeline = input("""Which lifeline do you want

                            1 ) 50/50
                            2) call a friend
                            3) Ask the audience
                            4)I dont want a life line

        Which lifeline do you choose """)
        if lifeline == "1":
            if player.fiftyused:
                print("You have used this lifeline chooses another one")
                lifelines(correct,lines,y,a,player)
            else:
                fifty(correct,lines,y,a,player)
        elif lifeline == "2":
            if player.callused:
                print("You have used this lifeline chooses another one")
                lifelines(correct,lines,y,a,player)
            else:
                call(correct,lines,y,a,player)
        elif lifeline == "3":
            if player.audienceused:
                print("You have used this lifeline chooses another one")
                lifelines(correct,lines,y,a,player)
            else:
                audience(correct,lines,y,a,player)
        else:
            pass

def fifty(correct,lines,y,a,player):
    number = random.randint(1,4)
    while number == correct:
        number = random.randint(1,4)
        
    print(correct, "=" ,a, "\t\t",number,"=" , lines[number + y])
    player.fifty()

def call(correct,lines,y,a,player):
    
    print(lines[correct])

    print("I think the answer is",a)
    
    player.call()

def audience(correct,lines,y,a,player):
    x = random.randint(50,100)
    y = random.randint(0,100-x)
    z = random.randint(0,100-x-y)
    v = 100 - (x + y + z)
    if correct == 1:
        print("1 =",x,"%\t2 =",y,"%\t3 =",z,"%\t4 =",v,"%\t")
        
    elif correct == 2:
        print("1 =",y,"%   2 =",x,"%   3 =",z,"%   4 =",v,"%\t")

    elif correct == 3:
        print("1 =",z,"%\t2 =",y,"%\t3 =",x,"%\t4 =",v,"%\t")
        
    elif correct == 4:
        print("1 =",v,"%\t2 =",y,"%\t3 =",z,"%\t4 =",x,"%\t")
    player.audience()
def main():
    intro()
    start_game()
    menu()

menu()
