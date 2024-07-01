import pygame
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
tamanio_ventana = (ANCHO_VENTANA, ALTO_VENTANA)
ventana = pygame.display.set_mode(tamanio_ventana)
fps = pygame.time.Clock()
pygame.display.set_caption("LOGOGAME")
logo = pygame.image.load("imagenes/logo.png")
pygame.display.set_icon(logo)