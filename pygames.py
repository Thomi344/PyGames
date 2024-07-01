import pygame
import sys
from funciones import *
from entradaysalidadedatos import *
from logos import *
from random import randint
from banderas import *
from setup import *
from colores import *
from imagenes import *
from sonidos import *
pygame.init()
pygame.mixer.init()

fondo = colocar_y_escalar_imagen("imagenes/Fondo_para_logo.png",tamanio_ventana)
ventana.blit(fondo, (0, 0))
#
ventana.blit(imagen_principal, (390, 80))
ventana.blit(imagen_play, (530, 475))
# #fuentes
fuente_principal = pygame.font.Font("Fuentes/VCR_OSD_MONO_1.001.ttf", 50)
fuente_secundaria = pygame.font.Font("Fuentes/Early GameBoy.ttf", 24)
fuente_limite = pygame.font.Font("Fuentes/VCR_OSD_MONO_1.001.ttf", 20)

# Carga de datos
path_csv = "resultados.csv"
lista_records = cargar_ultimo_resultado_csv(path_csv)
maximos_records = buscar_maximos_records(lista_records)

while ejecutar:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            ejecutar = False
        elif evento.type == pygame.TEXTINPUT:
            usuario += evento.text

        #si suelto las teclas pasa X cosa
        elif evento.type == pygame.KEYDOWN:
            #borro alguna letra en el usuario
            if evento.key == pygame.K_BACKSPACE:
                usuario = usuario[:-1]
            #cambio las banderas  y empiezo a contar
            elif evento.key == pygame.K_ESCAPE and escribir == True:
                tiempo_inicial = pygame.time.get_ticks()
                bandera_jugar = False
                escribir = True
                jugar = True
                
                reproducir_musica(music_principal,0.02)

        #recuadro ingresar usuario luego de darle al boton jugar
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            posicion_x, posicion_y = evento.pos

            if bandera_jugar and 530 <= posicion_x <= 730 and 475 <= posicion_y <= 675:
                ventana.blit(fondo_login, (0, 0))
                renderizar_texto(ventana,"Ingrese un usuario",BLANCO,fuente_principal,(368, 80))
                escribir = True
            
            elif jugar and 450 <= evento.pos[1] <= 720:  # Solo dentro del área de opciones
                click_x, click_y = evento.pos
                reloj = tiempo_transcurrido(tiempo_inicial, tiempo_actual)
                limite_x = determinar_limite_x(indice)

                #limites de click para las opciones correctas
                if limite_x <= click_x <= (limite_x + 320) and 450 <= click_y <= 720:
                    sound_coin.play()
                    monedas += 20
                    opcion_correcta = True 
                else:
                    sound_error.play()
                    opcion_incorrecta = True 
                    monedas -= 10
                    vidas -= 1

    #Si escribir esta en true       
    if escribir:
        #pinta el cuadro para poner el nombre
        recuadro_nombre = pygame.draw.rect(ventana, BLANCO, (390, 160, 480, 50), 0, 6)
        borde_recuadro_nombre = pygame.draw.rect(ventana, NEGRO, (390, 160, 480, 50), 4, 6)
        render = renderizar_texto_limite(usuario, fuente_principal, NEGRO, 440)
        ventana.blit(render, (395, 162))
        #si el usuario/nombre tiene mas de 10 letras
        if len(usuario) > 10:
            #escribe un mensaje 
            renderizar_texto(ventana,"Límite de 10 letras excedido",BLANCO,fuente_limite,(470, 215))
        elif len(usuario) > 1 and len(usuario) <= 10:
            #si el nombre tiene por lo menos una letra indica qué tecla tocar para continuar
            renderizar_texto(ventana, "Presione ESCAPE para continuar al juego", BLANCO, fuente_limite, (400,140))
        elif len(usuario) < 1:
            jugar = False

    #tiempo
    tiempo_actual = pygame.time.get_ticks()
    if jugar :
        escribir = False
        #Si matriz desordenada es igual a none (inicializada fuera del while),la desordena
        if matriz_desordenada == None:
            indice = randint(0, 3)
            matriz_desordenada = desordernar_matriz(matriz_opciones, indice)
        #un for que itera 4 veces
        for i in range(4):
            #carga el fondo del juego
            fondo_preguntas = colocar_y_escalar_imagen("imagenes/fondo pixelhd.png",(1280,450))
            ventana.blit(fondo_preguntas, (0,0))
            renderizar_texto(ventana," Cuál de los" ,BLANCO,fuente_principal,(450,150))
            renderizar_texto(ventana,"siguientes es el" ,BLANCO,fuente_principal,(420,200))
            renderizar_texto(ventana," logo correcto? " ,BLANCO,fuente_principal,(420,250))
            
            #acomoda las imagenes de la matriz
            acomodar_imagen = lambda x: x * 320 #LAMBDA multiplica X
            x = acomodar_imagen(i)
            imagen = matriz_desordenada[indice_fila_actual][i]#--------------
            imagen = pygame.transform.scale(imagen, (280, 230))
            posicion_imagen = (x + 20, 470)
            placa_opciones = pygame.draw.rect(ventana, GRIS, (x, 450, 320, 270))
            borde_placa_opciones = pygame.draw.rect(ventana, NEGRO, (x, 450, 320, 270), 3)
            ventana.blit(imagen, posicion_imagen)

        #pinta el reloj ,el tiempo,las monedas y su cantidad
        if opcion_correcta or descuento_vidas or opcion_incorrecta:
            tiempo_inicial = pygame.time.get_ticks()
            tiempo_resuelto = reloj
            acumulado_tiempo += tiempo_resuelto
            rondas +=1
            indice_fila_actual +=1
            opcion_correcta = False
            descuento_vidas = False
            opcion_incorrecta = False
            if indice_fila_actual >= len(matriz_desordenada):
                        indice_fila_actual = 0
                        
        reloj = tiempo_transcurrido(tiempo_inicial, tiempo_actual)
        tiempo_reloj = fuente_principal.render(f"{reloj}", False, BLANCO)
        total_monedas = fuente_principal.render(f"{monedas}", False, BLANCO)
        ventana.blit(total_monedas, (1150, 54))
        ventana.blit(tiempo_reloj, (1150, 124))
        ventana.blit(imagen_monedas, (1080, 54))
        ventana.blit(imagen_reloj, (1075, 121))
        distancia = 0
        
        #pinta los corazones
        imprimir_corazones(vidas, distancia,imagen_corazon, ventana)

        #Descuenta vidas cuando llega a 30
        if ((reloj != 0 and reloj % 30 == 0)) and descuento_vidas == False:
            descuento_vidas = True
            if vidas > 0:
                vidas -= 1
                sound_error.play()
                tiempo_general = tiempo_actual  
                siguiente_ronda = True
                indice_fila_actual += 1
                tiempo_inicial = pygame.time.get_ticks()
        
        #muestra pantalla final de juego terminado
        if vidas == 0 or rondas > 15:
            pygame.mixer_music.stop()
            if vidas == 0 :
                reproducir_musica("sonidos/Y2meta.app - Super Mario Bros - game over song (128 kbps).mp3",0.05)
            elif rondas > 15:
                reproducir_musica("sonidos/Y2meta.app - Música de Super Mario Bros. - Nivel Completo (128 kbps).mp3",0.05)
            ventana.blit(fondo_final,(0, 0))
            promedio_tiempo = round(acumulado_tiempo / rondas,1)
            texto_promedio = fuente_secundaria.render(f"El promedio de tiempo por ronda fue de {promedio_tiempo} segundos.", False, BLANCO)
            ventana.blit(texto_promedio, (20, 450))
            texto_monedas = fuente_secundaria.render(f"En total el usuario consiguio {monedas} monedas", False, BLANCO)
            ventana.blit(texto_monedas, (20, 550))
            ventana.blit(imagen_game_over, (160, 50))
            
            mensaje_record = mostrar_record(maximos_records, monedas)
            texto_record = fuente_secundaria.render(mensaje_record, False, BLANCO)
            ventana.blit(texto_record, (20, 650))
            jugar = False
    
    pygame.display.update()
    fps.tick(30)
nuevo_record = crear_nuevo_record(usuario,acumulado_tiempo,monedas,rondas-1)
lista_records = dar_de_alta_nuevo_record(lista_records,nuevo_record)
guardar_actualizacion_csv(lista_records,path_csv)
pygame.quit()
sys.exit()#cierra el programa correctamente