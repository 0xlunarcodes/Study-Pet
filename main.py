import pygame  

# pygame setup
#it can be a lil studying game that makes you want to study. possibly a todo list that will affect the status of the pet. 

pygame.init()
screen = pygame.display.set_mode((480, 480))
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
print(savedata[4])

savefile.close()

#variables
gameScreen = "title"
mouseclick = False
mouse = pygame.mouse.get_pos()
pygame.mixer.music.load("gamefiles/start.ogg")

#positions
dog_pos = pygame.Vector2(50,75)

#img/surfaces
gf_surf = pygame.image.load("gamefiles/gf.jpg").convert()
titledog_surf = pygame.transform.scale_by(pygame.image.load("dogpics/titledog.png").convert_alpha(), 1.5)
logo_surf = font_L.render('study dog !', True, textColor)
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

    match(gameScreen):
        case "title":
            #print("title screen")
            screen.blit(logo_surf, (100, 30))
            screen.blit(titledog_surf, (dog_pos))
                 
            #little cat image or whatever mikeila draws here
            
            #start button
            #start_surf is the button surface object, need to convert to rect object to get collision with mouse with colliedpoint
            screen.blit(start_surf, (135,400))
            if pygame.Rect((135, 400), start_surf.get_size()).collidepoint(mouse) and mouseclick: 
                print("button active")
                pygame.mixer.music.play()
                gameScreen = None
                #switch screen to either, new user screen or returning user screen. new user screen will have a tutorial or an explanation of what the app is for how to use etc

        case _:
            print("no current gamescreen!!")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pygame.quit()