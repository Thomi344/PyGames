import pygame
pygame.init()
pygame.mixer.init()

def tiempo_transcurrido(tiempo_inicial:int,tiempo_actual:int)->float:
    """
    Calcula el tiempo transcurrido desde el tiempo inicial hasta el momento actual.
    
    Args:
    tiempo_inicial (int): El tiempo inicial en ticks.
    
    Returns:
    float: El tiempo transcurrido en segundos.
    """
    tiempo_transcurrido = (tiempo_actual - tiempo_inicial) // 1000  # Convertir ticks a segundos
    return tiempo_transcurrido

def desordernar_matriz(matriz:list[list],indice:int)->list:
    """
    Reordena las filas de una matriz, insertando la última opción de cada fila en una nueva posición especificada.
    
    Args:
    matriz (list en lists): La matriz original con opciones.
    indice (int): La posición en la que se insertará la última opción de cada fila.
    
    Returns:
    list of lists: La nueva matriz con las opciones reordenadas.
    """
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = fila[:]  # Copia la fila sin la última opción correcta
        opcion_correcta = fila[-1]  # Obtiene la opción correcta (última de la fila original)
        nueva_fila.insert(indice, opcion_correcta)  # Inserta la opción correcta en la nueva posición
        nueva_matriz.append(nueva_fila)  # Añade la nueva fila a la nueva matriz
    return nueva_matriz

def renderizar_texto_limite(texto:str, fuente:tuple, color:tuple, limite_ancho:int):
    """
    Renderiza un texto utilizando la fuente y el color especificados, y lo recorta si excede el ancho límite.

    Args:
    texto (str): El texto a renderizar.
    fuente (pygame.font.Font): La fuente utilizada para renderizar el texto.
    color (tuple): El color del texto en formato RGB.
    limite_ancho (int): El ancho límite permitido para el texto renderizado.

    Returns:
    pygame.Surface: El texto renderizado, posiblemente recortado si excedía el ancho límite.
    """
    texto_renderizado = fuente.render(texto, True, color)
    if texto_renderizado.get_width() > limite_ancho:
        while texto_renderizado.get_width() > limite_ancho:
            texto = texto[:-1]
            texto_renderizado = fuente.render(texto, True, color)
    return texto_renderizado

def colocar_y_escalar_imagen(path:str,dimenciones:tuple):
    """
    Carga una imagen desde una ruta específica y la escala a las dimensiones dadas.

    Args:
    path (str): La ruta del archivo de imagen.
    dimensiones (tuple): Un par de enteros que representan las nuevas dimensiones (ancho, alto) de la imagen.

    Returns:
    pygame.Surface: La imagen escalada.
    """
    imagen =  pygame.image.load(path)
    imagen = pygame.transform.scale(imagen,dimenciones)
    return imagen

def buscar_maximos_records(lista: list[dict]) -> dict:
    """
    Busca el registro con el mayor número de monedas en una lista de diccionarios.

    Args:
    lista (list en dict): Una lista de diccionarios, donde cada diccionario representa un registro con un nombre y un número de monedas.

    Returns:
    dict: Un diccionario con el nombre del registro y el número máximo de monedas.
    """
    nombre_record = None
    record_monedas = 0
    maximo_monedas = -51
    
    for maximo in lista:
        if maximo['monedas'] > maximo_monedas:
            record_monedas = maximo['monedas']
            nombre_record = maximo['usuario']
            maximo_monedas = maximo['monedas']
    
    record = {"usuario": nombre_record,
            "monedas": record_monedas}

    return record

def renderizar_texto(ventana, texto,color,fuente, posicion):
    """
    Renderiza un texto en la ventana dada en la posición especificada.

    Args:
    ventana (pygame.Surface): La ventana o superficie donde se renderizará el texto.
    texto (str): El texto a renderizar.
    color (tuple): El color del texto en formato RGB.
    fuente (pygame.font.Font): La fuente utilizada para renderizar el texto.
    posicion (tuple): Un par de enteros que representan la posición (x, y) en la ventana donde se renderizará el texto.

    Returns:
    None
    """
    superficie_texto = fuente.render(texto, False, color)
    ventana.blit(superficie_texto, posicion)

def reproducir_musica (path:str,volumen:float):
    """
    Carga y reproduce un archivo de música desde una ruta específica, ajustando el volumen.

    Args:
    path (str): La ruta del archivo de música.
    volumen (float): El nivel de volumen para la reproducción (0.0 a 1.0).

    Returns:
    None
    """
    pygame.mixer_music.load(path)
    pygame.mixer_music.play()
    pygame.mixer_music.set_volume(volumen)
def cargar_sonido(ruta, volumen):
    """
    Carga un archivo de sonido desde una ruta específica y ajusta su volumen.

    Args:
    ruta (str): La ruta del archivo de sonido.
    volumen (float): El nivel de volumen para el sonido (0.0 a 1.0).

    Returns:
    pygame.mixer.Sound: El objeto de sonido cargado con el volumen ajustado.
    """
    sonido = pygame.mixer.Sound(ruta)
    sonido.set_volume(volumen)
    return sonido

def mostrar_record(maximos_records: list[dict], monedas: int)-> str:
    """
    Genera un mensaje indicando el estado actual del récord de monedas basado en una lista de máximos registros y el número de monedas del usuario actual.

    Args:
    maximos_records (dict): Un diccionario con las claves 'usuario' y 'monedas' que representan el nombre del usuario con el récord y el número máximo de monedas.
    monedas (int): El número de monedas del usuario actual.

    Returns:
    str: Un mensaje indicando el estado del récord de monedas.
    """
    if maximos_records['monedas'] == 0:
        maximos_records['usuario'] = "Nadie"
        mensaje_record = f"El record sigue siendo de {maximos_records['usuario']} con {maximos_records['monedas']} monedas"
    if maximos_records['monedas'] > monedas:
        mensaje_record = f"El record sigue siendo de {maximos_records['usuario']} con {maximos_records['monedas']} monedas"
    elif maximos_records['monedas'] < monedas: 
        mensaje_record = f"El record previo era de {maximos_records['monedas']} monedas"
    else:
        mensaje_record = f"Igualo el record previo de {monedas} monedas"
    
    return mensaje_record

def imprimir_corazones(vidas: int, distancia: int, imagen_corazon,ventana)-> None:
    """
    Dibuja imágenes de corazones en la ventana, una por cada vida restante.

    Args:
    vidas (int): El número de vidas restantes.
    distancia (int): La distancia inicial desde el borde izquierdo de la ventana para el primer corazón.
    imagen_corazon (pygame.Surface): La imagen del corazón a dibujar.
    ventana (pygame.Surface): La ventana o superficie donde se dibujarán los corazones.

    Returns:
    None
    """
    for corazon in range(vidas):
            ventana.blit(imagen_corazon, (40 + distancia, 54))
            distancia += 65

def determinar_limite_x(indice: int)-> int:
    """
    Determina el límite en el eje X según el índice proporcionado.

    Args:
    indice (int): El índice que determina el límite en el eje X (0, 1, 2, o 3).

    Returns:
    int: El límite en el eje X correspondiente al índice dado.
    """
    match indice:
        case 0:
            limite_x = 0
        case 1:
            limite_x = 320
        case 2:
            limite_x = 640
        case 3:
            limite_x = 960

    return limite_x