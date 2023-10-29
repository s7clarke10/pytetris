# pytetris.py
# import the pygame module, so you can use it
import pygame
import tetrispiece

# GLOBALS VARS
screen_width = 800
screen_height = 700

blocksize = tetrispiece.blocksize
grid_width = tetrispiece.grid_width
grid_height = tetrispiece.grid_height

grid_top_left_x = (screen_width - grid_width) // 2
grid_top_left_y = (screen_height - grid_height)

white_colour  = (255, 255, 255) # White RGB Colour
black_colour  = (0, 0, 0) # Black RGB Colour
grey_colour   = (169, 169, 169) # Grey RGB Colour
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("pytetris/images/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Py Tetris")
     
    # create a surface on screen that has the size of 800 x 700
    # Note the playing grid is a 10x20
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(grey_colour)

    # Draw the Tetris Grid boarder
    boarder = pygame.Rect(  grid_top_left_x,
                            grid_top_left_y,
                            grid_width,
                            grid_height) # X Pos, Y Pos, Width, Height
    pygame.draw.rect(screen, black_colour, boarder, 2)

    # Create Initial and Next Tetris Pieces
    tetris_piece = tetrispiece.Piece()
    next_tetris_piece = tetrispiece.Piece()

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tetris_piece.rotate()
                if event.key == pygame.K_LEFT:
                    tetris_piece.move_left()
                if event.key == pygame.K_RIGHT:
                    tetris_piece.move_right()
                if event.key == pygame.K_DOWN:
                    if tetris_piece.y_pos < grid_height - (blocksize * 3):
                        tetris_piece.move_down()
                    else:
                        tetris_piece = next_tetris_piece
                        next_tetris_piece = tetrispiece.Piece()

            tetris_piece.draw(screen)      
        
        pygame.display.update()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()