#reversi door Lewi Zeng(2236052) en Dylan Bloemendaal(9485961)

from tkinter import Frame, Toplevel, Label, Button, Entry
from typing import cast
from PIL.ImageDraw import ImageDraw
from PIL.ImageTk import PhotoImage
from PIL import Image

#scherm aanmaken
scherm = Frame()
cast(Toplevel,scherm.master).title("Reversi")
scherm.configure(background="white")
scherm.configure(width=500, height=500)
scherm.pack()
plaatje = Image.new(mode="RGBA", size=(500,500))
afbeelding = Label(scherm)
afbeelding.place(x=0, y=0)
afbeelding.configure(background="white")
draw = ImageDraw(plaatje)

#aanmaken van knopen en tekst
aantalR = Label(scherm)
aantalB = Label(scherm)

helpknop = Button(scherm)
nieuw = Button(scherm)

kolom = Entry(scherm)
rij = Entry(scherm)

ktekst = Label(scherm)
rtekst = Label(scherm)
maak = Button(scherm)

uitkomst = Label(scherm)

#positie van knoppen en aantal stenen
aantalR.place(x = 30, y = 15)
aantalB.place(x = 30, y = 40)

helpknop.place(x = 150, y = 15)
nieuw.place(x = 260, y  = 15)

kolom.place(x = 450, y = 15)
rij.place(x = 450, y = 40)

ktekst.place(x = 400, y = 15)
rtekst.place(x = 400, y = 40)
maak.place(x = 400, y = 65)

uitkomst.place(x = 200, y = 450)

#tekst voor knoppen
helpknop.configure(width = 10, text = "help")
nieuw.configure(width = 10, text = "nieuw spel")
maak.configure(width = 10, text = "maak bord")

#invoer van grootte bord
kolom.configure(width = 2)
rij.configure(width = 2)

ktekst.configure(width = 5, text = "kolom:", background = "white")
rtekst.configure(width = 3, text = "rij:", background = "white")

#tekst voor de aantal stenen per speler
aantalR.configure(text = "0 stenen", background = "white")
aantalB.configure(text = "0 stenen", background = "white")
draw.ellipse(((10, 18), (20, 28)), fill = "red")
draw.ellipse(((10, 43), (20, 53)), fill = "blue")

#in het begin is de uitkomst onzichtbaar, als er een uitkomst is dan pas tekst laten verschijnen
uitkomst.configure(width = 18, text = "", background = "white")

#rand van spelbord(spelbord altijd even groot)

#vakjes(moet een functie worden omdat de speler de bord grootte kan kiezen)
def vakjes(x:int, y:int) -> None:
    draw.rectangle(((90, 100), (400, 400)), fill = "white", outline = "black")
    t = 0
    n = 0
    k = 310/x
    r = 300/y
    k2 = 90
    r2 = 100
    for t in range(0, x):
        draw.line(((k2, 100), (k2, 400)), "black")
        k2 = k2 + k
    for n in range(0, y):
        draw.line(((90, r2), (400, r2)), "black")
        r2 = r2 + r

#invoer van speler(de labels lezen als de speler de "maak bord" knop heeft ingedrukt)(WIP)



#invoer van speler in de vakjes functie zetten(WIP)
def coords():
    xcoord = int(rij.get())
    ycoord = int(kolom.get())
    vakjes(xcoord, ycoord)
    global foto
    foto = PhotoImage(plaatje)
    afbeelding.configure(image=foto)

#coords = [[(y,x) for x in range(lengte)] for y in range(breedte)]

vakjes(6,6)

#tekst van wie de winnar is of remise(WIP)
def uitkomst() -> None:
    winner = 1
    #rood en blauw naar 1 veranderen als er eentje wint(WIP)
    rood = 0
    blauw = 0
    if rood == winner:
        uitkomst.confiugure(text = "rood heeft gewonnen")
    elif blauw == winner:
        uitkomst.configure(text = "blauw heeft gewonnen")
    else:
        uitkomst.configure(text = "de game is geëindigd remise")


maak.configure(command = coords)
foto = PhotoImage(plaatje)
afbeelding.configure(image=foto)
scherm.mainloop()
