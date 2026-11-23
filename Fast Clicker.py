from tkinter import *
import time
    
timer =""
print("What time do you want ?")
print("1. 5 seconds")
print("2. 10 seconds")
print("3. 30 seconds")
timer= input("Enter your choice : ")
print("Click the space barre !")
if (timer == "1") :
    start_time = time.time()  
    
    score=0
    def keyPressed(event):
        keysym=event.keysym
        #print(event.keysym, event.keysym==' ')
        if keysym == "space":
            global score
            score = score + 1
            print(score)
        if (time.time() - start_time) >= 5 :
            # root.destroy()
            print("It's over !")
            root.destroy()
            
    root = Tk()
    root.bind("<KeyRelease>", keyPressed)
    root.mainloop()
    
