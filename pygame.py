'''___________________________________________________________________________
Wszystkie importy'''

from Tkinter import*
from PIL import Image, ImageTk

import pygame
import random


'''___________________________________________________________________________
Wszystkie funkcje'''


puzzle = ""


def losuj_puzzle:
    ilosc_puzzli = 6
    global wylosowane_puzzle
    wylosowane_puzzle = []
    for i in range(ilosc_puzzli):
        wylosowane_puzzle+= random.choice(puzzle)
        

def wyswietl_wylosowane_puzzle:
    print(wylosowane_puzzle)

def dodaj_jeden:
    if len(wylosowane_puzzle)<6:
        wylosowane_puzzle.append(random.choice(puzzle))

'''___________________________________________________________________________
okono gry'''


okno_gry = Tk()
okno_gry.title("Zamkowe sprzataczki - gra puzzle")
okno_gry.geometry("350x200")


#wczytanie obrazu tła
plotno.pack()
background_image=Image.open('castle.jpg')
background_imageTk=ImageTk.Photoimage(background_image)
plotno.create_image(350, 200,image=background_imageTk)

#wczytanie grafiki protagonisty gry
protag_image=Image.open('protag.png')
protag_imageTk=ImageTk.Photoimage(protag_image)
plotno.create_image(20, 8,image=protag_imageTk)

przycisk_losuj_puzzle = Button(okno_gry, text="Losuj puzle",fg="red",command = losuj_puzzle, command = wyswietl_wylosowane_puzzle, command= dodaj_jeden)
przycisk_losuj_puzzle.pack(side=BOTTOM)

okno_gry.mainloop()
