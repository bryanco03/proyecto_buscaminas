import pygame
import os
from boton import Button


class Game():

    def __init__(self,tablero,tamaño):
        self.tablero = tablero
        self.tamaño =  tamaño
        self.tamaño_casilla =  self.tamaño[0] // self.tablero.get_size()[1], self.tamaño[1] // self.tablero.get_size()[0]
        self.cargar_imagenes()


    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.tamaño)
        pygame.display.set_caption("Buscaminas")
        #self.bg = pygame.image.load("assets/Background.png")
        self.menu()

        #running =  True
        #while running:
        #    for event in pygame.event.get():
        #        if (event.type == pygame.QUIT):
        #            running = False 
        #        if (event.type == pygame.MOUSEBUTTONDOWN):
        #            posicion = pygame.mouse.get_pos()
        #            right_click = pygame.mouse.get_pressed()[2]
        #            self.handleclick(posicion,right_click)

        #    self.mostrar()
        #    pygame.display.flip()
        #    if self.tablero.get_ganar():
        #        running= False
        #pygame.quit()


    def menu(self):
        while True:
            #self.screen.blit((0, 0))

            menu_posicion = pygame.mouse.get_pos()

            menu_texto = self.get_font(75).render("Buscaminas", True, "#b68f40")
            MENU_RECT = menu_texto.get_rect(center=(400, 200))

            boton_play = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 350), text_input="JUGAR", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            boton_opciones = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 550),text_input="OPCIONES", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            boton_salir = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 700), text_input="QUIT", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(menu_texto, MENU_RECT)

            for button in [boton_play, boton_opciones, boton_salir]:
                button.changeColor(menu_posicion)
                button.update(self.screen)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_play.checkForInput(menu_posicion):
                        pass
                        self.play()
                    if boton_opciones.checkForInput(menu_posicion):
                        pass
                        #options()
                    if boton_salir.checkForInput(menu_posicion):
                        pygame.quit()
                        #sys.exit()

            pygame.display.update()

    def play(self):

        running =  True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False 
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    posicion = pygame.mouse.get_pos()
                    right_click = pygame.mouse.get_pressed()[2]
                    self.handleclick(posicion,right_click)
            self.mostrar()
            pygame.display.flip()
            if self.tablero.get_ganar():
                running= False
        pygame.quit()





    def mostrar(self):
        top_left = (0,0)
        for row in range(self.tablero.get_size()[0]):
            for col in range(self.tablero.get_size()[1]):
                casilla = self.tablero.get_casilla((row,col)) 
                imagen = self.get_imagen(casilla)
                self.screen.blit(imagen,top_left)
                top_left = top_left[0] + self.tamaño_casilla[0], top_left[1]
            top_left = 0, top_left[1]  + self.tamaño_casilla[1]

    def handleclick(self,posicion,right_click):
        if (self.tablero.get_perder()):
            return
        index = posicion[1] //self.tamaño_casilla[1] , posicion[0] // self.tamaño_casilla[0]
        casilla = self.tablero.get_casilla(index)
        self.tablero.handleclick(casilla,right_click)

    def get_font(self,tamaño):
        return pygame.font.Font("assets/font.ttf",tamaño)


    def cargar_imagenes(self):
        self.images = {}
        for filename in os.listdir("images"):
            if (not filename.endswith(".png")): 
                continue # Ignorar los archivos que no son png
            imagen = pygame.image.load(r"images/" + filename)
            imagen = pygame.transform.scale(imagen, self.tamaño_casilla)
            self.images[filename.split(".")[0]] = imagen


    def get_imagen(self,casilla):
        string = None
        if casilla.get_clicked():
            string = "bomb-at-clicked-block" if casilla.get_bomba() else str(casilla.get_num_alrededor())
        else:
            string = "flag" if casilla.get_bandera() else "empty-block"
        return self.images[string]