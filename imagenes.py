from funciones import colocar_y_escalar_imagen
import pygame
from setup import *

# Imagen de presentación y comienzo del juego
imagen_principal = pygame.transform.scale(logo, (500, 500))
imagen_play = colocar_y_escalar_imagen("imagenes/iconos/play.png", (200,200))
#IMAGENES
imagen_monedas = colocar_y_escalar_imagen("imagenes/iconos/moneda.png",(50, 50))
imagen_reloj = colocar_y_escalar_imagen("imagenes/iconos/reloj.png",(60,60))
imagen_corazon = colocar_y_escalar_imagen("imagenes/iconos/corazon.png",(70,70))
imagen_game_over = colocar_y_escalar_imagen("imagenes/iconos/game over.png", (960, 360))
fondo_final = colocar_y_escalar_imagen("imagenes/fondo_negro.jpg", (1280,720))
fondo_login = colocar_y_escalar_imagen("imagenes/Fondo_login.png", (1280,720))