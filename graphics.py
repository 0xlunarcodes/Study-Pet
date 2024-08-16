import pygame
#fonts
pygame.init()
textColor = (48, 74, 57)

font_L = pygame.font.Font("gamefiles/Daydream.ttf", 30)
font_M = pygame.font.Font("gamefiles/Daydream.ttf", 20)
font_S = pygame.font.Font("gamefiles/Daydream.ttf", 10)

font_L.render('study dog !', True, textColor)

surfaces = {} #Surface Dictionary

def genText(name, text, size) :
    if size == "s" :
        font = font_S
    elif size == "m" :
        font = font_M
    else :
        font = font_L
    
    new_surf = font.render(text, True, textColor)
    surfaces[name + "Surf"] = new_surf
    print(name + "Surf Created")