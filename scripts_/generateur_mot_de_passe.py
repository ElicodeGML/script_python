from tkinter import *

# crée fenetre
window = Tk()
window.title("Generateur de mot de passe")
window.geometry("720x480")
# window.iconbitmap("imagess copy.ico")
window.config(background="#BF4768")

# cree frame principale
frame = Frame(window, bg="#BF4768")
frame.pack()

# creation d'image
widths = 300
heigths = 300
image = PhotoImage(file="images/imagess copy.png").zoom(35).subsample(35)
canvas = Canvas(frame, width=widths, height=heigths, bg="#BF4768", bd=0, highlightthickness=0)
canvas.create_image(widths/2, heigths/2, image=image)
canvas.pack()

# cree titre
label_titl = Label(frame, text="Mot de passe", font=("Helvetica", 20), bg="#BF4768", fg="white")
label_titl.pack()

# afficher fenetre
window.mainloop()
