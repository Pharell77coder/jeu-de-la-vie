import pygame, random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 20
HEIGHT = 20

MARGIN = 1
max_column = 70
max_row = 35
grid = [[random.choice([True,False]) for x in range( max_column )] for y in range( max_row )]
FPS = 1


WINDOW_SIZE = [(MARGIN + HEIGHT) * max_column  + MARGIN, (MARGIN + HEIGHT) * max_row + MARGIN]
screen = pygame.display.set_mode( WINDOW_SIZE )

pygame.display.set_caption( "Array Backed Grid" )

done = False

clock = pygame.time.Clock()
années = 0
while not done :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            column = pos [0] // (WIDTH + MARGIN)
            row = pos [1] // (HEIGHT + MARGIN)
            grid [row] [column] = True
            print( "Click ", pos, "Grid coordinates: ", row, column, grid [row] [column] )



    screen.fill( BLACK )

    # Draw the grid
    for row in range( max_row ) :
        for column in range( max_column ) :
            color = 'white'
            voisin = 0
            if row+1 != max_row:
                if grid[row+1][column]:
                    voisin += 1
            else :
                if grid[0][column]:
                    voisin += 1
            if column + 1 != max_column :
                if grid[row][column+1]:
                    voisin += 1
            else :
                if grid[row][0]:
                    voisin += 1
            if row != 0:
                if grid[row-1][column]:
                    voisin += 1
            else:
                if grid[max_row-1][column]:
                    voisin += 1
            if column != 0 :
                if grid[row][column-1]:
                    voisin += 1
            else :
                if grid[row][max_column-1]:
                    voisin += 1


            if row+1 != max_row and column + 1 != max_column :
                if grid[row+1][column+1]:
                    voisin += 1
            else :
                if grid[0][0]:
                    voisin += 1

            if column + 1 != max_column  and row != 0 :
                if grid[row-1][column+1]:
                    voisin += 1
            else :
                if grid[max_row-1][0]:
                    voisin += 1
            if row != 0  and column + 1 != max_column :
                if grid[row-1][column+1]:
                    voisin += 1
            else:
                if grid[max_row-1][0]:
                    voisin += 1
            if column != 0 and row != 0 :
                if grid[row-1][column-1]:
                    voisin += 1
            else :
                if grid[max_row-1][max_column-1]:
                    voisin += 1


            if voisin == 3:
                grid [row] [column] = True
            elif voisin > 3 or voisin < 2:
                grid [row] [column] = False
            else:
                pass

            if grid [row] [column]:
                color = 'red'#(random.randint(0,255), random.randint(0,255), random.randint(0,255))

            pygame.draw.rect( screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])



    clock.tick(FPS)

    pygame.display.flip()


pygame.quit()