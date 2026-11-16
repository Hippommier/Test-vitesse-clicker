from test_module import testFunction
from fastClicker import gameClicker

#on cree un menu principale avec "play et exit"
playing = False
choice = ""
testFunction(playing)

#test(jsp comment ca marche, voir video)
while True:
    
    print("1. PLAY")
    print("2. Quit")
    
    choice = input("Enter your choice : ")
    choice = choice.strip()
    
    if(choice == "1"):
        print("ok start program")
        playing = True
        #mtn il faut "activer" le play
        break
    elif (choice =="2"):
        print("bye")
        break
    else:
        print("invalid option. please try again!")
        
#ca marche? let's goooo
#mtn faut que le bouton "play" fasse qqch...comment?