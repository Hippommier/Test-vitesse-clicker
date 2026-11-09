#on cree un menu principale avec "play et exit"

choice = ""
#test(jsp comment ca marche, voir video)
while True:
    
    print("1. PLAY")
    print("2. Quit")
    
    choice = input("Enter your choice : ")
    choice = choice.strip()
    
    if(choice == "1"):
        print("ok start program")
        #mtn il faut "activer" le play
        break
    elif (choice =="2"):
        break
    else:
        print("invalid option. please try again!")
        
#ca marche? let's goooo
#mtn faut que le bouton "play" fasse qqch...comment?