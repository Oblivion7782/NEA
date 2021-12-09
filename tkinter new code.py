from pygame import *

blueC = (0, 110, 255)
whiteC = (255)

class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        ###################
        
def update(self):
    ############
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    gameState = GameState.TITLE
    #########

def titleScreen(screen):
    startButton= UIELEMENT(
        centrePosition = (400,200),
        fontSize = 30,
        bg_rgb = blueC,
        text_rgb = whiteC,
        text = "Start"
        action = GameState.##############################()
        )
    helpButton= UIELEMENT(
        centrePosition = (400,300),
        fontSize = 30,
        bg_rgb = blueC,
        text_rgb = whiteC,
        text = "Help"
        action = GameState.HELP
        )
    settingsButton= UIELEMENT(
        centrePosition = (400,400),
        fontSize = 30,
        bg_rgb = blueC,
        text_rgb = whiteC,
        text = "Settings"
        action = GameState.Settings
        )
    quitButton = UIElement(
        centerPosition=(400, 500),
        fontSize=30,
        bg_rgb=blueC,
        text_rgb=whiteC,
        text="Quit",
        action=GameState.QUIT,
    )
    
    buttons = [startButton, helpButton, settingsButton, quitButton]
    
    while True:
         mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
