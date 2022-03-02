import random



x=1
computer=0
user=0

while x!=4:
    print("Computer Score: "+str(computer))
    print("Your Score: "+str(user))
    
    print("Choose One of This Option by Input The Number: ")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissor")
    print("4.Exit")
    print("Your Choice(By Number)")
    x=int(input())
    
    computer_choice=random.randint(1,3)
    
    if(x==1):
        print("Your Choice: Rock")
    elif(x==2):
        print("Your Choice: Paper")
    elif(x==3):
        print("Your Choice: Scissor")   
    
    if(computer_choice==1):
        print("Computer Choice: Rock")
    elif(computer_choice==2):
        print("Computer Choice: Paper")
    elif(computer_choice==3):
        print("Computer Choice: Scissor")
    
    if(x==1 and computer_choice==2):
        computer=computer+1
    elif(x==2 and computer_choice==1):
        user=user+1
    elif(x==1 and computer_choice==3):
        user=user+1
    elif(x==3 and computer_choice==1):
        computer=computer+1
    elif(x==2 and computer_choice==3):
        computer=computer+1
    elif(x==3 and computer_choice==2):
        user=user+1
    
    print(" ")