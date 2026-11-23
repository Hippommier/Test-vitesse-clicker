#on va coder un des jeux de clicker en random qui sera ma partie du mvp	
#helpSvp
import random
import time
#faut generer une lettre aleatoire
print("Welcome to random letter clicker, a game where you need to click many random generated number in a chosen time")
timerr = int(input("choose a time (in seconds) : "))
#print("to start, press space")
#il faut que la touche espace (space) lance le jeu
score = 0
#le program génère aléqtoirement des lettres
letters = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]
#le compte a rebours de wish
depart = time.monotonic()

while (time.monotonic() - depart) < timerr:
    randomletter = random.choice(letters)
    print(randomletter)
    rep = str(input())
    if rep == randomletter :
        score += 1
perc = float(score / timerr)
print(f"game over ! score : {score} percentage : {perc}")
#ptn ca marche!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



