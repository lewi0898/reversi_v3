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
plaatje = Image.new(mode="RGBA", size=(500,500), color="white")
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
nieuw.place(x = 260, y = 15)

kolom.place(x = 450, y = 15)
rij.place(x = 450, y = 40)

ktekst.place(x = 400, y = 15)
rtekst.place(x = 400, y = 40)
maak.place(x = 400, y = 65)

uitkomst.place(x = 150, y = 450)

#tekst voor knoppen
helpknop.configure(width = 10, text = "help")
nieuw.configure(width = 10, text = "nieuw spel")
maak.configure(width = 10, text = "maak bord")

#invoer van grootte bord
kolom.configure(width = 2)
rij.configure(width = 2)

kolom.insert(0, "6")
rij.insert(0, "6")

ktekst.configure(width = 5, text = "kolom:", background = "white")
rtekst.configure(width = 3, text = "rij:", background = "white")

#tekst voor de aantal stenen per speler
aantalR.configure(text = "0 stenen", background = "white")
aantalB.configure(text = "0 stenen", background = "white")
draw.ellipse(((10, 18), (20, 28)), fill = "red")
draw.ellipse(((10, 43), (20, 53)), fill = "blue")

#in het begin is de uitkomst onzichtbaar
uitkomst.configure(width = 28, text = "", background = "white")

#variabelen voor het spel
xcoord = 6
ycoord = 6
speler = "red"
bord = []
klaar = False


#rand van spelbord
def vakjes(x:int, y:int) -> None:
    draw.rectangle(((90, 100), (400, 400)), fill = "white", outline = "black")
    t = 0
    n = 0
    k = 310/x
    r = 300/y
    k2 = 90
    r2 = 100

    for t in range(0, x + 1):
        draw.line(((k2, 100), (k2, 400)), "black")
        k2 = k2 + k

    for n in range(0, y + 1):
        draw.line(((90, r2), (400, r2)), "black")
        r2 = r2 + r


#het bord maken met de ingevoerde grootte
def coords():
    global xcoord, ycoord, bord, speler, klaar

    try:
        xcoord = int(kolom.get())
        ycoord = int(rij.get())
    except ValueError:
        uitkomst.configure(text = "Vul geldige getallen in")
        return

    #bord moet minimaal 4 bij 4 zijn en even afmetingen hebben
    if xcoord % 2 == 1 or ycoord % 2 == 1:
        uitkomst.configure(text = "Gebruik even getallen")
        return

    if xcoord < 4 or ycoord < 4 or xcoord > 16 or ycoord > 16:
        uitkomst.configure(text = "Gebruik getallen tussen 4 en 16")
        return

    speler = "red"
    klaar = False

    #lege lijst voor het bord maken
    bord = []

    for y in range(ycoord):
        regel = []
        for x in range(xcoord):
            regel.append(0)
        bord.append(regel)

    #vier beginstenen in het midden
    middenx = xcoord // 2
    middeny = ycoord // 2

    bord[middeny - 1][middenx - 1] = "red"
    bord[middeny][middenx] = "red"

    bord[middeny - 1][middenx] = "blue"
    bord[middeny][middenx - 1] = "blue"

    stenen_tekenen()
    stenen_tellen()

    uitkomst.configure(text = "Rood is aan de beurt")


#stenen tekenen op het bord
def stenen_tekenen():
    vakjes(xcoord, ycoord)

    k = 310 / xcoord
    r = 300 / ycoord

    for y in range(ycoord):
        for x in range(xcoord):

            if bord[y][x] != 0:
                x1 = 90 + x * k + 3
                y1 = 100 + y * r + 3
                x2 = 90 + (x + 1) * k - 3
                y2 = 100 + (y + 1) * r - 3

                draw.ellipse(((x1, y1), (x2, y2)), fill = bord[y][x])

    global foto
    foto = PhotoImage(plaatje)
    afbeelding.configure(image = foto)


#aantal stenen van beide spelers tellen
def stenen_tellen():
    rood = 0
    blauw = 0

    for y in range(ycoord):
        for x in range(xcoord):

            if bord[y][x] == "red":
                rood = rood + 1

            if bord[y][x] == "blue":
                blauw = blauw + 1

    aantalR.configure(text = str(rood) + " stenen")
    aantalB.configure(text = str(blauw) + " stenen")


#controleren of een zet geldig is en welke stenen omgedraaid worden
def controleren(x, y, kleur):
    stenen = []

    #controleren of het vakje leeg is
    if bord[y][x] != 0:
        return stenen

    #kleur van de tegenstander bepalen
    if kleur == "red":
        tegenstander = "blue"
    else:
        tegenstander = "red"

    #alle 8 richtingen controleren
    for richtingx in range(-1, 2):
        for richtingy in range(-1, 2):

            if richtingx == 0 and richtingy == 0:
                continue

            tijdelijk = []

            nieuwx = x + richtingx
            nieuwy = y + richtingy

            #zoeken naar stenen van de tegenstander
            while nieuwx >= 0 and nieuwx < xcoord and nieuwy >= 0 and nieuwy < ycoord:

                if bord[nieuwy][nieuwx] == tegenstander:
                    tijdelijk.append((nieuwx, nieuwy))

                elif bord[nieuwy][nieuwx] == kleur:

                    if len(tijdelijk) > 0:
                        stenen = stenen + tijdelijk

                    break

                else:
                    break

                nieuwx = nieuwx + richtingx
                nieuwy = nieuwy + richtingy

    return stenen


#controleren of een speler nog een zet kan doen
def kan_spelen(kleur):
    for y in range(ycoord):
        for x in range(xcoord):

            if len(controleren(x, y, kleur)) > 0:
                return True

    return False


#een steen plaatsen wanneer op het bord wordt geklikt
def plaatsen(event):
    global speler, klaar

    if klaar == True:
        return

    #positie van de muis
    x = event.x
    y = event.y

    #controleren of er binnen het bord wordt geklikt
    if x < 90 or x >= 400 or y < 100 or y >= 400:
        return

    #berekenen op welk vakje is geklikt
    k = 310 / xcoord
    r = 300 / ycoord

    vakx = int((x - 90) / k)
    vaky = int((y - 100) / r)

    #controleren of de zet geldig is
    stenen = controleren(vakx, vaky, speler)

    if len(stenen) == 0:
        uitkomst.configure(text = "Ongeldige zet")
        return

    #steen plaatsen
    bord[vaky][vakx] = speler

    #stenen van de tegenstander omdraaien
    for steen in stenen:
        x = steen[0]
        y = steen[1]

        bord[y][x] = speler

    stenen_tekenen()
    stenen_tellen()

    #andere speler is aan de beurt
    if speler == "red":
        speler = "blue"
    else:
        speler = "red"

    #controleren of de nieuwe speler kan spelen
    if kan_spelen(speler) == False:

        #terug naar de vorige speler
        if speler == "red":
            speler = "blue"
        else:
            speler = "red"

        #als beide spelers niet kunnen spelen is het afgelopen
        if kan_spelen(speler) == False:
            klaar = True
            winnaar()
            return

        if speler == "red":
            uitkomst.configure(text = "Blauw slaat over, rood is aan de beurt")
        else:
            uitkomst.configure(text = "Rood slaat over, blauw is aan de beurt")

    else:
        if speler == "red":
            uitkomst.configure(text = "Rood is aan de beurt")
        else:
            uitkomst.configure(text = "Blauw is aan de beurt")


#tekst van wie de winnaar is of remise
def winnaar() -> None:
    rood = 0
    blauw = 0

    for y in range(ycoord):
        for x in range(xcoord):

            if bord[y][x] == "red":
                rood = rood + 1

            if bord[y][x] == "blue":
                blauw = blauw + 1

    if rood > blauw:
        uitkomst.configure(text = "rood heeft gewonnen")

    elif blauw > rood:
        uitkomst.configure(text = "blauw heeft gewonnen")

    else:
        uitkomst.configure(text = "de game is geÃ«indigd in remise")


#nieuw spel met dezelfde bordgrootte
def opnieuw():
    coords()


#helpknop
def help():
    uitleg = Toplevel()
    uitleg.title("Help")
    uitleg.geometry("350x200")

    tekst = Label(uitleg, text =
        "Reversi spelregels:\n\n"
        "Rood begint.\n"
        "Klik op een vakje om een steen te plaatsen.\n"
        "Je moet een steen van de tegenstander insluiten.\n"
        "Ingesloten stenen veranderen van kleur.\n"
        "Als je niet kunt zetten, sla je een beurt over.\n"
        "De speler met de meeste stenen wint."
    )
    tekst.pack()

#tekenen van de mogelijke plek
def help_tekenen():
    vakjes(xcoord, ycoord)

    k = 310 / xcoord
    r = 300 / ycoord

    for y in range(ycoord):
        for x in range(xcoord):

            if bord[y][x] != 0:
                x1 = 90 + x * k + 3
                y1 = 100 + y * r + 3
                x2 = 90 + (x + 1) * k - 3
                y2 = 100 + (y + 1) * r - 3

                draw.ellipse(((x1, y1), (x2, y2)), fill = bord[y][x])

    #hstenen = controleren()

    global foto
    foto = PhotoImage(plaatje)
    afbeelding.configure(image = foto)



#knoppen koppelen aan functies
maak.configure(command = coords)
nieuw.configure(command = opnieuw)
helpknop.configure(command = help)

#muisklikken op het bord
afbeelding.bind("<Button-1>", plaatsen)

#standaard een bord van 6 bij 6 maken
coords()

scherm.mainloop()