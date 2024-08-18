import pygame
#fonts
pygame.init()

#text specific variables
textColor = (48, 74, 57)
font_L = pygame.font.Font("gamefiles/Daydream.ttf", 30)
font_M = pygame.font.Font("gamefiles/Daydream.ttf", 20)
font_S = pygame.font.Font("gamefiles/Daydream.ttf", 10)
textDict = {} #Surface Dictionary

#image specific variables
imageDict = {}

#pygame.Rect((80, 275), start_surf.get_size()).collidepoint(mouse) and mouseclick

class ImageObj :
    def __init__(self, surface, position=None) :
        self.surf = surface
        self.pos = position
    
    def get(self) :
        print(self.surf, self.pos)
        return(self.surf, self.pos)
    
    def isClicked(self, mousePosition, mouseClick) -> bool :
        if (pygame.Rect(self.pos, self.surf.get_size())).collidepoint(mousePosition) and mouseClick :
            return True
        else :
            return False
class TextObj:    
    def __init__(self, surface, position=None):
        self.surf = surface
        self.pos = position
        print("Text Obj Init")
        
    def get(self) :
        return (self.surf, self.pos)
    
    def getColor(self) :
        return self.surf.textColor
    
def genText(name, text, position=None, size=None) :         
    if size == "S" :
        font = font_S
    elif size == "L" :
        font = font_L
    else :
        font = font_M
        
    new_surf = font.render(text, True, textColor)
    textDict[name] = TextObj(new_surf, position)
    
def genImage(name, image, position=None, transparency=None, scale=None) :
    if transparency == True :
        newSurf = pygame.image.load_extended(image).convert_alpha()
        print("timg init")
    else :
        newSurf = pygame.image.load(image).convert()
        print("img init")
    if scale != None :
        newSurf = pygame.transform.scale_by(newSurf, scale)
        imageDict[name] = ImageObj(newSurf,position)
    else :
        imageDict[name] = ImageObj(newSurf,position)   
        
#if image pos,  image surf size.collidepoint mouse, and mouse click