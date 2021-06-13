#1. elementy dotyczące puzzli (klasa Puzzel)
# 1a każdy obiekt puzzel ma właściwości, które umożliwiają poruszanie się (cztery kierunki --> wasd)
# 1b żeby umożliwić poruszanie się puzzlem, puzzel musi być zaznaczony (zaznaczony puzzel zmienia kolor)
# 1c klikniecie w plansze odznacza zaznaczony puzzel
#2. klasa Puzzle służąca do obsługiwania puzzli (dokładanie elementów)

'''___________________________________________________________________________
Wszystkie importy'''
import pygame
from  tkinter import *
from tkinter import messagebox
import random


'''___________________________________________________________________________
Wszystkie funkcje'''

def przycisk_instrukcja():
    messagebox.showinfo("Instrukcja gry",'Witamy w naszej grze!\n\nTwoim celem jest:\n  obrócenie ścieżki tak, by dało się po niej przejść; \n  posprzątanie jej; \n  ucieczka przed lawą. \n\nZaznaczanie puzzli: kliknięcie myszką\n    UWAGA! Po kliknięciu kolejnego puzzla NIE MOŻESZ\n    wrócić do obracania poprzedniego!\nObrót puzzli: klawisze WSAD\nSprzątanie: kliknięcie myszką\n    UWAGA! Jeśli nie sprzątniesz, nie ruszysz się dalej\n    postacią!\nSterowanie postacią: strzałki\n\nW górnym polu ekranu zobaczysz Twój pasek zdrowia.\nPośpiesz się! Zmniejsza się szybciej niż byś chciał!')

def przycisk_authors():
    messagebox.showinfo('Autorki', text = 'Freaking awesome code authors:\nNatalia Szantar\nKornelia Winiarska\nMartna Świątek\nPatrycja Lelujko\n\n\nFreaking awesome concept authors:\nNatalia Szantar\nKornelia Winiarska\nMartna Świątek\nPatrycja Lelujko\n\n\nFreaking awesome graphic character designer:\nKornelia Winiarska\n\n\nNot really freaking awesome music themes performer:\nMartna Świątek')

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

global selected
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
        self.aktywny=0
    


    def click(self):
        if self.aktywny==0:
            print('super', self.x, self.y)
            zdj=PhotoImage(file='graphics/path/'+self.name+'_pressed.png')
            self.puzzel.configure(image=zdj)
            self.puzzel.image = zdj
            global selected
            selected = self.numer
            puzzle.zaznacz(self.numer)
            self.aktywny=1
    def odznacz(self):
        zdj=PhotoImage(file='graphics/path/'+self.name+'.png')
        self.puzzel.configure(image=zdj)
        self.puzzel.image = zdj
    def place(self, x, y):
        self.x=x
        self.y=y
        self.puzzel.place(x=x*50, y=y*50)
    def move(self, x, y):
        if self.x+x>=2 and self.x+x<7 and self.y+y>=2 and self.y+y<7:
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

    def odznacz_wszystko(self):
        for i in range(len(self.p)):
            if i!=selected:
                self.p[i].odznacz()

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
            self.p[selected].move(0,1)

    def przesun_w_gore(self):
        if selected!=-1:
            print('przesun_w_gore()')
            self.p[selected].move(0,-1)
    
    def hoover(self, x, y):
        x0=x//50
        y0=y//50
        for i in range(len(self.p)):
            self.p[i].hoover(x0, y0)

    
def keypress(event):
    if event.char == 'd':
        print('keypress()')
        puzzle.przesun_w_prawo()
        move_value += 1
    elif event.char == 'a':
        puzzle.przesun_w_lewo()
        move_value += 1
    elif event.char=='w':
        puzzle.przesun_w_gore()
        move_value += 1
    elif event.char=='s':
        puzzle.przesun_w_dol()
        move_value += 1
    else:
        pass

puzzle=Puzzle()
puzzle.zaznacz(2)

#wczytanie obrazów puzzli
puzzle.append(Puzzel('prawodol', 4, 2,0))
puzzle.append(Puzzel('prawodol', 3, 2,1))
puzzle.append(Puzzel('prawogora', 4, 3,2))
puzzle.append(Puzzel('lewogora', 4, 4,3))
puzzle.append(Puzzel('prosto', 4, 5,4))
puzzle.append(Puzzel('prosto', 3, 5,5))
puzzle.append(Puzzel('lewodol', 4, 6,6))


#pobieranie współrzędnych kursora myszy
def click(event):
 #   if do_capture:
    #x, y = event.x_root, event.y
    #print('{}, {}'.format(x, y))
    puzzle.odznacz_wszystko()
okno_gry.bind('<ButtonRelease-1>', click)

okno_gry.bind('d',keypress)
okno_gry.bind('a', keypress)
okno_gry.bind('w', keypress)
okno_gry.bind('s', keypress)


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


#class tworzenie_puzzli:
 #   def __init__(self, okienko):
  #      self.okno_gry = okienko
   #     self.numery_puzzli = []
    #    self.stworz_puzzle()

    #def stworz_puzzle(self):
     #   del self.numery_puzzli[:]
      #  while len(self.numery_puzzli) != 12:
       #     numer = random.randint(1, 12)
        #    if numer not in self.numery_puzzli:
         #       self.numery_puzzli.append(numer)
        #print (self.numery_puzzli)

        #return self.numery_puzzli

    #def wyswietl_puzzle(self,numery_puzzli):
     #   zmienna_x = 1
      
    #  zmienna_y = 1
     #   puzzle = []
      #  for numer_puzzla in numery_puzzli:
       #    puzzle.append(DigitSqr(self.screen, digit, 100 * counter_x, 100 * counter_y))
        #   counter_x += 1
         #  if zmienna_x % 4 == 0:
          #     zmienna_x = 1
           #    zmienna_y += 1

        #return puzzle



# wyświetlanie okienka z instrukcją gry

instrukcja = Button(okno_gry, text = "Instrukcja gry", command =  przycisk_instrukcja)
instrukcja.pack(side=LEFT)
autorki = Button(okno_gry, text = 'Autorki', command = przycisk_authors)
autorki.pack()


okno_gry.mainloop()

#changes/marge
