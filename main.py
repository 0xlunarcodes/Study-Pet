import pygame  
import graphics
# pygame setup
#it can be a lil studying game that makes you want to study. possibly a todo list that will affect the status of the pet. 

pygame.init()
screen = pygame.display.set_mode((360, 360))
clock = pygame.time.Clock()
running = True
dt = 0 #deltatime

#fonts
font_L = pygame.font.Font("gamefiles/Daydream.ttf", 30)
font_M = pygame.font.Font("gamefiles/Daydream.ttf", 20)
font_S = pygame.font.Font("gamefiles/Daydream.ttf", 10)

#colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
bgColor = (137, 199, 156)
textColor = (48, 74, 57)

#savadata
#creates savedata if not exist, writes default values
savefile = open("gamefiles/savedata.txt", "r")
savedata= savefile.readlines()
savefile.close()

print(savedata[0])

#variables
gameScreen = "title"
mouseclick = False
mouse = pygame.mouse.get_pos()
pygame.mixer.music.load("gamefiles/start.ogg")

#positions
dog_pos = pygame.Vector2(50,55)

#img/surfaces
graphics.genText('title', 'study dog !', 'l')
gf_surf = pygame.image.load("gamefiles/gf.jpg").convert()
titledog_surf = (pygame.image.load("dogpics/titledog.png").convert_alpha())
start_img = pygame.image.load_extended("gamefiles/start.png").convert_alpha()
start_surf = pygame.transform.scale_by(start_img, 4)


while running:    
    mouse = pygame.mouse.get_pos()
    dt = clock.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
            
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouseclick = True
            
            
        if event.type == pygame.MOUSEBUTTONUP:
            mouseclick = False


    screen.fill(bgColor)

    # all previous code in this while loop deals with events, framerate and clearing the previous frame. 
    #other code , actual code for the game in the while loop will go below this line
    
    status_surf = font_S.render(f"<3 {savedata[0].rstrip(savedata[0][-1])}!  hunger {savedata[1].rstrip(savedata[1][-1])}!  intel {savedata[2].rstrip(savedata[2][-1])}!", True, textColor)


    match(gameScreen):
        case "title":
            #print("title screen")
            screen.blit(graphics.surfaces['titleSurf'], (40, 10)) #Boss, we figured it out, time to build outer haven
            screen.blit(titledog_surf, (dog_pos))
                 
            
            #start button
            #start_surf is the button surface object, need to convert to rect object to get collision with mouse with colliedpoint
            screen.blit(start_surf, (80,275))
            if pygame.Rect((80, 275), start_surf.get_size()).collidepoint(mouse) and mouseclick: 
                print("button active")
                pygame.mixer.music.play()
                gameScreen = "main"
                
        case "main" : 
            #print(savedata[1])
            screen.blit(status_surf, (40, 10))
            screen.blit(titledog_surf, (dog_pos))
                  

        case _:
            print("no current gamescreen!!")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pygame.quit()