from importlib.abc import ResourceReader
import os
from random import randrange
import sys
from tkinter import*
#-----------------------------------------------------------Paramètres de la fenêtre------------------------------------------------------
app = Tk()
app.title("Chifoumi")
app.geometry("500x350")
app.resizable(False, False)
app["bg"]="#c8b6ff"
#-----------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------Variables et fonctions-------------------------------------------------------------
actions=["Pierre", "Papier", "Ciseaux"]
global jscore 
jscore = 0
global rscore
rscore = 0

def resetcmd():
  global jscore
  jscore = 0
  global rscore
  rscore = 0
  annonce["text"] = ""
  annonce2["text"] = ""
  joueur["text"] = f"Toi : {jscore}"
  robot["text"] = f"Robot : {rscore}"

def joue(action):
  global jscore
  global rscore
  actrob = actions[randrange(0, 3)]
  annonce["text"] = ""
  annonce2["text"] = ""
  if action == actrob:
    annonce["text"] = f"{action} VS {actrob}: Égalité !"
  elif ((action == "Pierre") and (actrob == "Ciseaux")) or ((action == "Papier") and (actrob == "Pierre")) or ((action == "Ciseaux") and (actrob == "Papier")):
    annonce["text"] = f"{action} VS {actrob}: Bien joué !"
    annonce2["text"] = f"{action} gagne face à {actrob}"
    jscore += 1
    joueur["text"] = f"Toi : {jscore}"
  else:
    annonce["text"] = f"{action} VS {actrob}: Dommage :("
    annonce2["text"] = f"{actrob} gagne face à {action}"
    rscore += 1
    robot["text"] = f"Robot : {rscore}"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#-----------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------En-tête--------------------------------------------------------------------
label = Label(app, text="Bienvenue au jeu du Chifoumi", font=("Arial, 22"), bg="#c8b6ff")
label.pack(side=TOP, pady=5)
info = Label(app, text="Choisissez votre action", font=('Arial, 10'), bg="#c8b6ff")
info.pack(side=TOP, pady=5)
#-----------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------Script principal----------------------------------------------------------------
frame = Frame(app, bg="#c8b6ff")
frame.pack()
options = {"padx": 10, "pady": 10, "anchor": N}

pierre = PhotoImage(file = resource_path("assets\pierre.png"))
pierreimage = pierre.subsample(3,3)
pierrebutton = Button(frame, text="Pierre", image=pierreimage, compound=LEFT, bg="#ffd6ff", activebackground="#ecd3ff", command= lambda: joue("Pierre"))
pierrebutton.pack(side=LEFT, **options)

papier = PhotoImage(file = resource_path("assets\papier.png"))
papierimage = papier.subsample(3,3)
papierbutton = Button(frame, text="Papier", image=papierimage, compound=LEFT, bg="#ffd6ff", activebackground="#ecd3ff", command= lambda: joue("Papier"))
papierbutton.pack(side=LEFT, **options)

ciseaux = PhotoImage(file = resource_path("assets\ciseaux.png"))
ciseauximage = ciseaux.subsample(3,3)
ciseauxbutton = Button(frame, text="Ciseaux", image=ciseauximage, compound=LEFT, bg="#ffd6ff", activebackground="#ecd3ff", command= lambda: joue("Ciseaux"))
ciseauxbutton.pack(side=LEFT, **options)

annonce = Label(app, text="", font =('Arial, 15'), bg="#c8b6ff")
annonce.pack()
annonce2 = Label(app, text="", font =('Arial, 15'), bg="#c8b6ff")
annonce2.pack()

resetbutton = Button(text="Reset", bg="#ffd6ff", activebackground="#ecd3ff", font=('Arial, 12'), command=resetcmd)
resetbutton.pack(pady=10)

joueur = Label(app, text=f"Toi : {jscore}", font =('Arial, 12'), bg="#c8b6ff")
joueur.pack(anchor=SW)
robot = Label(app, text=f"Robot : {rscore}", font =('Arial, 12'), bg="#c8b6ff")
robot.pack(anchor=SW)
#------------------------------------------------------------------------------------------------------------------------------------------

app.mainloop()