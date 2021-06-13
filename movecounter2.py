pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 25)
#licznik ruchów
move_value = 0

mvX = 350 #(POŁOŻENIE MOVE COUNTERA X - DO DOSTOSOWANIA)
mvY = 300 #(POŁOŻENIE MOVE VOUNTERA Y - DO DOSTOSOWANIA)

def how_much_moves(x, y):
    move_counter = font.render("Moves:" + " " + str(move_value), True, (225, 225, 225))
    screen.blit(move_counter, (x, y))
    
#w głównej pętli  
    how_much_moves(mvX, mvY)
#update'y move countera w poszczególnych patchach do funkcji/pętli
