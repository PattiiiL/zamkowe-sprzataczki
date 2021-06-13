'''___________________________________________________________________________
Wszystkie importy'''

from  tkinter import *
from tkinter import messagebox

'''___________________________________________________________________________
Wszystkie funkcje'''

def przycisk_instrukcja():
    messagebox.showinfo("Instrukcja gry","Gra zamkowe sprzataczki dzieli sie na 3 etapy:\n W pierwszym etapie trzeba ułożyć puzzle w taki sposób aby tworzyły spójną ścieżkę. \n Następnie poruszając się za pomocą strzałek należy przejść postacią po ścieżce\n przez zamek do miejsca docelowego, zanim zapadnie się podłoga.")


'''___________________________________________________________________________
okono gry'''
okno_gry = Tk()
okno_gry.title("Gra zamkowe sprzataczki")
okno_gry.geometry("600x600")


#wczytanie obrazu tła
tlo_zamek=PhotoImage(file="graphics/background/castle.png")
tlo=Label(okno_gry, image=tlo_zamek)
tlo.place(x=0,y=0)

#wczytanie obrazów puzzli
puzzle_prawodol_zdj=PhotoImage(file='graphics/path/prawo_dol.png')
puzzle_prawodol=Label(okno_gry, image=puzzle_prawodol_zdj)
puzzle_prawodol.place(x=190, y=100) 

puzzle_prawogora_zdj=PhotoImage(file='graphics/path/prawo_gora.png')
puzzle_prawogora=Label(okno_gry, image=puzzle_prawogora_zdj)
puzzle_prawogora.place(x=190, y=150)

puzzle_lewogora_zdj=PhotoImage(file='graphics/path/lewo_gora.png')
puzzle_lewogora=Label(okno_gry, image=puzzle_lewogora_zdj)
puzzle_lewogora.place(x=190, y=200)

puzzle_prosto_zdj=PhotoImage(file='graphics/path/prosto.png')
puzzle_prosto=Label(okno_gry, image=puzzle_prosto_zdj)
puzzle_prosto.place(x=190, y=250)

puzzle_lewodol_zdj=PhotoImage(file='graphics/path/lewo_dol.png')
puzzle_lewodol=Label(okno_gry, image=puzzle_lewodol_zdj)
puzzle_lewodol.place(x=190, y=300)

#wczytanie grafiki protagonsty
protag_zdj=PhotoImage(file='graphics/protagonist/protag.png')
protag=Label(okno_gry, image=protag_zdj)
protag.place(x=200, y=400)



#wyswietlenie okienka z instrukcje gry

instrukcja = Button(okno_gry, text = "Instrukcja gry", command =  przycisk_instrukcja)
instrukcja.pack(side=LEFT)


okno_gry.mainloop()
