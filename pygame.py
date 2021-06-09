'''___________________________________________________________________________
Wszystkie importy'''
import pygame
from game.digit_sqr import DigitSqr
from  tkinter import *
from tkinter import messagebox
import random


'''___________________________________________________________________________
Wszystkie funkcje'''

def przycisk_instrukcja():
    messagebox.showinfo("Instrukcja gry","Gra zamkowe sprzataczki dzieli sie na 3 etapy:\n W pierwszym etapie trzeba ułożyć puzzle w taki sposób aby tworzyły spójną ścieżkę. \n Następnie poruszając się za pomocą strzałek należy przejść postacią po ścieżce\n przez zamek do miejsca docelowego, zanim zapadnie się podłoga.")


'''___________________________________________________________________________
okono gry'''
okno_gry = Tk()
okno_gry.title("Gra zamkowe sprzataczki")
okno_gry.geometry("600x600")


'''___________________________________________________________________________
wczytywanie grafiki'''

# wczytanie obrazu tła
tlo_zamek=PhotoImage(file="graphics/background/castle.png")
tlo=Label(okno_gry, image=tlo_zamek)
tlo.place(x=0,y=0)

selected=-1
class Puzzel:
    def __init__(self,name, x, y, numer):
        self.name=name
        zdj=PhotoImage(file='graphics/path/'+name+'.png')
        self.puzzel=Label(okno_gry, image=zdj)
        self.puzzel.configure(image=zdj)
        self.puzzel.image = zdj
        self.place(x,y)
        self.puzzel.bind("<ButtonRelease-1>", lambda event: self.click())
        self.numer=numer
        

    def click(self):
        print('super', self.x, self.y)
        zdj=PhotoImage(file='graphics/path/'+self.name+'_pressed.png')
        self.puzzel.configure(image=zdj)
        self.puzzel.image = zdj
        selected=self.numer
        puzzle.zaznacz(self.numer)
    def place(self, x, y):
        self.x=x
        self.y=y
        self.puzzel.place(x=x*50, y=y*50)
    def move(self, x, y):
        self.x+=x
        self.y+=y
        self.puzzel.place(x=self.x*50, y=self.y*50)
    def hoover(self, x, y):
        if self.x==x and self.y==y:
            zdj=PhotoImage(file='graphics/path/prosto_pressed.png')
            self.puzzel.configure(image=zdj)
            self.puzzel.image = zdj
        else:
            zdj=PhotoImage(file='graphics/path/prosto.png')
            self.puzzel.configure(image=zdj)
            self.puzzel.image = zdj

    

class Puzzle:
    def __init__(self):
        self.p=[]
        selected=1
        

    def append(self, puzzel):
        self.p.append(puzzel)

    def zaznacz(self, numer):
        selected=numer
    
    

    def przesun_w_prawo(self):
        if selected!=-1:
            print('przesun_w_prawo()')
            self.p[selected].move(1,0)

    def przesun_w_lewo(self):
        if selected!=-1:
            print('przesun_w_lewo()')
            self.p[selected].move(-1,0)

    def przesun_w_dol(self):
        if selected!=-1:
            print('przesun_w_dol()')
            self.p[selected].move(0,-1)

    def przesun_w_gore(self):
        if selected!=-1:
            print('przesun_w_gore()')
            self.p[selected].move(0,1)
    
    def hoover(self, x, y):
        x0=x//50
        y0=y//50
        for i in range(len(self.p)):
            self.p[i].hoover(x0, y0)

    
def keypress(event):
    if event.char == 'd':
        print('keypress()')
        puzzle.przesun_w_prawo()
    elif event.char == 'a':
        puzzle.przesun_w_lewo()
    elif event.char=='w':
        puzzle.przesun_w_gore()
    elif event.char=='s':
        puzzle.przesun_w_dol()
    else:
        pass

puzzle=Puzzle()
puzzle.zaznacz(2)

#wczytanie obrazów puzzli
puzzle.append(Puzzel('prawodol', 4, 2,0))
puzzle.append(Puzzel('prawogora', 4, 3,1))
puzzle.append(Puzzel('lewogora', 4, 4,2))
puzzle.append(Puzzel('prosto', 4, 5,3))
puzzle.append(Puzzel('lewodol', 4, 6,4))


#pobieranie współrzędnych kursora myszy
def motion(event):
 #   if do_capture:
    x, y = event.x_root, event.y
    print('{}, {}'.format(x, y))
    #puzzle.hoover(x,y)
okno_gry.bind('<Motion>', motion)

okno_gry.bind('d',keypress)
okno_gry.bind('a', keypress)
okno_gry.bind('w', keypress)
okno_gry.bind('s', keypress)
# wczytanie obrazów puzzli i stworzenie duszkow z poszczegolnymi puzzlami

#puzzle_prawodol_zdj=PhotoImage(file='graphics/path/prawodol.png')
#puzzle_prawodol=Label(okno_gry, image=puzzle_prawodol_zdj)
#puzzle_prawodol.place(x=190, y=100)


def capture(flag):
    global do_capture
    do_capture = flag

#def choose_puzzle():
    #puzzle_prostoselected_zdj=PhotoImage(file='graphics/path/prosto_selected.png')
    #puzzle_prosto.configure(image=puzzle_prostoselected_zdj)
    #puzzle_prosto.image = puzzle_prostoselected_zdj

#def press_puzzle():
 #   puzzle_prostopressed_zdj=PhotoImage(file='graphics/path/prosto_pressed.png')
  #  puzzle_prosto.configure(image=puzzle_prostopressed_zdj)
   # puzzle_prosto.image = puzzle_prostopressed_zdj

    
capture(False)
#okno_gry.bind("<ButtonPress-1>", lambda event: choose_puzzle())
#okno_gry.bind("<ButtonRelease-1>", lambda event: capture(False))

# wczytanie grafiki protagonsty
protag_zdj=PhotoImage(file='graphics/protagonist/protag.png')
protag=Label(okno_gry, image=protag_zdj)
protag.place(x=200, y=400)

'''___________________________________________________________________________
tworzenie klasy puzzle'''


class tworzenie_puzzli:
    def __init__(self, okienko):
        self.okno_gry = okienko
        self.numery_puzzli = []
        self.stworz_puzzle()

    def stworz_puzzle(self):
        del self.numery_puzzli[:]
        while len(self.numery_puzzli) != 12:
            numer = random.randint(1, 12)
            if numer not in self.numery_puzzli:
                self.numery_puzzli.append(numer)
        print (self.numery_puzzli)

        return self.numery_puzzli

    def wyswietl_puzzle(self,numery_puzzli):
        zmienna_x = 1
        zmienna_y = 1
        puzzle = []
        for numer_puzzla in numery_puzzli:
           puzzle.append(DigitSqr(self.screen, digit, 100 * counter_x, 100 * counter_y))
           counter_x += 1
           if zmienna_x % 4 == 0:
               zmienna_x = 1
               zmienna_y += 1

        return puzzle
'''___________________________________________________________________________
realizowanie reguły can't touch the floor:'''

#zakrywanie puzzli za pomoca czerwonych kwadratów

class Czerwony_kwadrat:

    def __init__(self):
        a = 50 
        b = 50
        # a i b to odpowiedznio szerokość i wysokość, które są stałe dla każdego kwadratu

    def tworzenie_kwadratu(self,x,y):
        kwadrat = pygame.rect(x,y, self.a, self.b) 
        pygame.draw.rect(screen,(255,50,50),kwadrat) # w nawiasie kolejno: msc wyświetlenia, kolor jako krotka, to co chcemy narysować
        pygame.display.flip() #umożliwia wyświetlenie kwadratu na planszy

#tworzenie obiektow klasy Czerwony_kwadrat
kwardat = Czerwony_kwadrat()

#zasłanianie puzzli po kolei z użyciem modułu time = realizowanie reguły can't touch the floor

i = 5 # i = liczba puzzli do zakrycia
zmienna_x = 200
zmienna_y = 100

while i != 0:
    kwardat.tworzenie_kwadratu(zmienna_x, zmienna_y) # używając metod klasy rysujemy kolejne kwadraty
    time.sleep(10) #ustawiamy odstęp pomiędzy zasłanianiem kolejnych puzzli na 10 sek
    i -= 1 
    zmienna_y += 50 


#wyświetlenie okienka z instrukcją gry

instrukcja = Button(okno_gry, text = "Instrukcja gry", command =  przycisk_instrukcja)
instrukcja.pack(side=LEFT)


okno_gry.mainloop()
