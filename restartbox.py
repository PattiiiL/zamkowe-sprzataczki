from tkinter import *
#mamy chyba gdzieś import time

#moja propozycja na wrzucenie tego? bo nie znalazłam komendy jako tako game over
def show_game_over(x,y):
    game_over = font.render("GAME OVER", True, (0,0,0))
    screen.blit(game_over, (x,y))
    time.sleep(10)
    restart_game.mainloop()

restart_game = Tk()
want_restart = IntVar()

#funkcja restart
def restarting_game():
    if want_restart == 1:
        win_theme.stop() or loose_theme.stop()
        running = True
    else:
        running = False

#okno restart wyskakujące
do_want_restart = Label(restart_game, text = 'Do you want to play again?')
do_want_restart.pack()

want_restart_yes = Radiobutton(restart_game, text = 'Yes', variable = want_restart, value=1)
want_restart_yes.pack(side=LEFT)
want_restart_no = Radiobutton(restart_game, text = 'No', variable = want_restart, value=2)
want_restart_no.pack(side=RIGHT)
checking = Button(restart_game, text = 'OK', command = restarting_game)
checking.pack(side=BOTTOM)


