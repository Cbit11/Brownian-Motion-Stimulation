import numpy as np
import pygame

black = (0,0,0)
white = (255,255,255)
BALL_SPEED= 25
dim = 420
x1, y1, =1,1
def right_collide(rect: list, radius:float, center:list):
    #[430, 170, 850, 590]
    if center[0]> rect[2]-radius:
        return True
    return False
def left_collide(rect: list, radius:float, center:list):
    #[430, 170, 850, 590]
    if center[0]< rect[0]+radius:
        return True
    return False
def up_collide(rect: list, radius:float, center:list):
    #[430, 170, 850, 590]
    if center[1]> rect[3]-radius:
        return True
    return False
def down_collide(rect: list, radius:float, center:list):
    #[x:430, y:170, x:850, y:590]
    if center[1]< rect[1]+radius:
        return True
    return False
def main():
    circle_x, circle_y= 1280//2, 720//2
    pygame.init()
    window = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    ball_dir= pygame.math.Vector2(1,0)
    rect1= pygame.Rect(430,170,420,420)
    stimulation_run= False
    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # fill the screen with a color to wipe away anything from last frame
        window.fill("white")
        #draw the rect
        pygame.draw.rect(window, black,rect1,width=1)

        #draw the ball
        pygame.draw.circle(window, 'red',(circle_x, circle_y),15)
    # RENDER YOUR GAME HERE
        circle_x+=ball_dir.x* BALL_SPEED*x1
        circle_y+= ball_dir.y* BALL_SPEED*y1
        
        if left_collide([430, 170, 850, 590], 15, [circle_x, circle_y]):
            #ball_dir= pygame.math.Vector2(1,0)
            ball_dir.x= np.random.rand()
            ball_dir.y= np.random.normal(0,0.1)
        if right_collide([430, 170, 850, 590], 15, [circle_x, circle_y]):
            # ball_dir= pygame.math.Vector2(-1,0)
            ball_dir.x= -np.random.rand()
            ball_dir.y= np.random.normal(0,0.1)
        if up_collide([430, 170, 850, 590], 15, [circle_x, circle_y]):
            # ball_dir= pygame.math.Vector2(0,-1)
            ball_dir.x= np.random.normal(0,0.1)
            ball_dir.y= -np.random.rand()
        if down_collide([430, 170, 850, 590], 15, [circle_x, circle_y]):
            # ball_dir= pygame.math.Vector2(0,1)     
            ball_dir.x= np.random.normal(0,0.1)
            ball_dir.y= np.random.rand()

        if circle_x> 850 or circle_y> 590 or circle_x<430 or circle_y<170:
            running= False
    # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()