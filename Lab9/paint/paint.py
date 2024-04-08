import pygame

def main():
    pygame.init()
    W = 640
    H = 480
    
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    
    radius = 15
    points = []

    # current states
    mode = "blue"
    figure = "circle"
    
    # eraser flag
    flag_eraser = False
    
    # figures
    square_figure = pygame.draw.rect(screen, (100, 100, 100), (10, 10, 50, 50))
    circle_figure = pygame.draw.circle(screen, (100, 100, 100), (95, 35), 25)
    rectangle_figure = pygame.draw.rect(screen, (100, 100, 100), (120, 10, 75, 50))
    
    # colors
    red_color = pygame.draw.rect(screen, (255, 0, 0), (W - 110, 10, 20, 50))
    green_color = pygame.draw.rect(screen, (0, 255, 0), (W - 70, 10, 20, 50))
    blue_color = pygame.draw.rect(screen, (0, 0, 255), (W - 50, 10, 20, 50))
    
    # eraser
    eraser_font = pygame.font.SysFont("comicsansms", 30)
    eraser_text = eraser_font.render("Click E to toggle eraser", True, (255, 255, 255))
    eraser_text_rect = eraser_text.get_rect()
    eraser_text_rect.bottom = H - 10
    eraser_text_rect.right = W - 10
    
    while True:
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = "red"
                    points = []
                elif event.key == pygame.K_g:
                    mode = "green"
                    points = []
                elif event.key == pygame.K_b:
                    mode = "blue"
                    points = []

                # determine if a eraser was toggled
                if event.key == pygame.K_e:
                    flag_eraser = not flag_eraser    
                    points = []

                # determine if a figure was changed
                if event.key == pygame.K_z:
                    figure = "circle"
                elif event.key == pygame.K_x:
                    figure = "square"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if square_figure.collidepoint(mousePos):
                    figure = "square"
                    points = []
                elif circle_figure.collidepoint(mousePos):
                    figure = "circle"
                    points = []
                elif rectangle_figure.collidepoint(mousePos):
                    figure = "rectangle"
                    points = []
                elif r_triangle_figure.collidepoint(mousePos):
                    figure = "right triangle"
                    points = []
                elif e_triangle_figure.collidepoint(mousePos):
                    figure = "equilateral triangle"
                    points = []
                elif rhombus_figure.collidepoint(mousePos):
                    figure = "rhombus"
                    points = []
                elif red_color.collidepoint(mousePos):
                    mode = "red"
                    points = []
                elif green_color.collidepoint(mousePos):
                    mode = "green"
                    points = []
                elif blue_color.collidepoint(mousePos):
                    mode = "blue"
                    points = []
                else:
                    if event.button == 1: # left click grows radius
                        radius = min(200, radius + 1)
                    elif event.button == 3: # right click shrinks radius
                        radius = max(1, radius - 1)
                    
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]  
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, flag_eraser, figure)
            i += 1
        
        # draw menu
        pygame.draw.rect(screen, (25, 25, 25), (0, 0, W, 70))
        square_figure = pygame.draw.rect(screen, (200, 200, 200) if figure == "square" else (100, 100, 100), (10, 10, 50, 50))
        circle_figure = pygame.draw.circle(screen, (200, 200, 200) if figure == "circle" else (100, 100, 100), (95, 35), 25)
        rectangle_figure = pygame.draw.rect(screen, (200, 200, 200) if figure == "rectangle" else (100, 100, 100), (130, 10, 75, 50))
        r_triangle_figure = pygame.draw.polygon(screen, (200, 200, 200) if figure == "right triangle" else (100, 100, 100), ((215, 10), (215, 60), (265, 60)))
        e_triangle_figure = pygame.draw.polygon(screen, (200, 200, 200) if figure == "equilateral triangle" else (100, 100, 100), ((300, 10), (275, 60), (325, 60)))
        rhombus_figure = pygame.draw.polygon(screen, (200, 200, 200) if figure == "rhombus" else (100, 100, 100), ((335, 35), (360, 10), (385, 35), (360, 60)))
        red_color = pygame.draw.rect(screen, (255, 89, 94), (W - 70, 10, 20, 50))
        green_color = pygame.draw.rect(screen, (138, 201, 38), (W - 50, 10, 20, 50))
        blue_color = pygame.draw.rect(screen, (25, 130, 196), (W - 30, 10, 20, 50))
        
        screen.blit(eraser_text, eraser_text_rect)
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, flag_eraser, figure):
    if not flag_eraser:
        c1 = max(0, min(255, 2 * index - 256))
        c2 = max(0, min(255, 2 * index))

        if color_mode == "blue":
            color = (c1, c1, c2)
        elif color_mode == "red":
            color = (c2, c1, c1)
        elif color_mode == "green":
            color = (c1, c2, c1)
    else:
        color = (0, 0, 0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if figure == "circle":
            pygame.draw.circle(screen, color, (x, y), width)
        elif figure == "square":
            pygame.draw.rect(screen, color, (x - width, y - width, 2 * width, 2 * width))
        elif figure == "rectangle":
            pygame.draw.rect(screen, color, (x - 1.5 * width, y - width, 3 * width, 2 * width))
        elif figure == "right triangle":
            pygame.draw.polygon(screen, color, ((x - width, y - width), (x - width, y + width), (x + width, y + width)))
        elif figure == "equilateral triangle":
            pygame.draw.polygon(screen, color, ((x, y - width), (x - width, y + width), (x + width, y + width)))
        elif figure == "rhombus":
            pygame.draw.polygon(screen, color, ((x - width, y), (x, y - width), (x + width, y), (x, y + width)))

main()