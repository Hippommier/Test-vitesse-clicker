
def playprog() :
    jeu = ""
    choicetwo = ""



while True:
    
    print("1. Fast Clicker")
    print("2. Random Letter")
    
    choicetwo = input("Enter your choice : ")
    choicetwo = choicetwo.strip()
    
    if(choicetwo == "1"):
        print("Fast Clicker : be ready ! ")
        fast = True
        jeu = fast
        break
    elif (choicetwo =="2"):
        print("Random Letter : Good luck !")
        random = True
        jeu = random
        break
    else:
        print("invalid option. please try again!")
    
    
    
