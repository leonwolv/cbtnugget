import circle as c, drawcircle as d, pygame

running = True


d.setup()

while running:
    ev = pygame.event.get()


    for event in ev:

        if event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()

            c1 = c.Circle()
            c1.radius  = 25
            c1.x = pos[0]
            c1.y = pos[1]
            c1.color = "red"
            c1.filled = True
            

            d.drawCircle(c1)
            pygame.display.update()
        
        if event.type == pygame.QUIT:
            running = False