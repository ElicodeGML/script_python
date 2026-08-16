 # importer mon app de fentre
from tkinter import *

import webbrowser

def open_graven_channel():
    webbrowser.open_new('https://www.tf1.fr/tf1/ici-tout-commence/videos/ici-tout-commence-du-15-aout-2023-episode-730-62604552.html')

 # ma fenetre
window = Tk()

 # titre
window.title("Mon app")
 # taille de l'app
window.geometry("720x480")
 # taille min
window.minsize(0, 0)
 # taille max
window.maxsize(2000, 2000)
 # couleur du fond
window.config(background='#12B3B3')

 # boite d'ecriture
frame = Frame(window, bg='#12B3B3', bd=1, relief=SUNKEN)
 # premier texte
label_title = Label(frame, text="Bienvenue",
                    font=("Courrier", 30), bg='#12B3B3', fg='white')
label_title.pack(expand='YES')

 # deuxieme texte
label_subtitle = Label(frame, text="épisode 730",
                    font=("Courrier", 20), bg='#12B3B3', fg='white')

yt_button = Button(frame, text="Ici tout commence",
                    font=("Courrier", 30), bg='white', 
                    fg='#12B3B3', command=open_graven_channel)
 # afficher  et mettre au centre de l'image ma boite 
 # et mon texte au centre de la boite
label_subtitle.pack()
frame.pack(expand='yes')
yt_button.pack(pady=25, fill='x')

 # ouvrire dans un pop-up
window.mainloop()
