#wszystkie themes

main_theme = pygame.mixer.Sound('main_theme_jb.mp3')
win_theme = pygame.mixer.Sound('win_theme_dre.mp3')
lose_theme = pygame.mixer.Sound('loose_theme_mw.mp3')

#main theme dodawany do main loop
running = True
  while running:
      screen.blit(background_Img,(0,0))
      main_theme.play()

#do fragmentu natalii and mojego o game_over

collision = collisionTrue(protagX, protagY, roomX, roomY)
if collision:
    show_score(scoreX, scoreY)
    main_theme.stop()
    show_game_over(game_overX, game_overY)
    time.sleep(1)
    win_theme.play()
if current_health<=0:
    current_health = 0
    main_theme.stop()
    show_game_over(game_overX, game_overY)
    time.sleep(1)
    lose_theme.play()
if score_value<=0:
        score_value = 0
        main_theme.stop()
        show_game_over(game_overX, game_overY)
        time.sleep(1)
        lose_theme.play()
