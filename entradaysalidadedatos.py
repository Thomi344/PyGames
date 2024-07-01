##################  CSV  ##################
#----------Cargar---------

def cargar_ultimo_resultado_csv(path:str)->list[dict]:
    """
    Carga los datos del ultimo record desde un archivo CSV.

    Args:
        path (str): La ruta del archivo CSV que contiene los datos de las records.

    Returns:
        list[dict]: Una lista de diccionarios que contiene los datos de las records cargadas desde el archivo CSV.
    """

    archivo = open(path,mode='r',encoding='utf-8')
    lineas = archivo.readlines() #lee lineas
    archivo.close()
    lista_records = []
    for i in range(1,len(lineas)):#lee linea por linea,arranca desde el indice uno porque el 0 no nos sirve ya que es la info

        datos = lineas[i] #representa los datos de los resultados (es un str)
        datos = datos.split(",") #se convierte en una lista de sublistas desde la coma,Guardo los datos en sus respectivos indices en variables
        if len (datos) == 5 : #si la lista datos es igual a 7
            identificacion =int(datos[0]) #casteo los datos porque son enteros
            usuario = datos[1]
            tiempo = datos[2]
            monedas = int(datos[3])
            rondas = (datos[4])
            rondas = rondas.replace("\n","") #remplazo el \n por nada
            rondas =  int(rondas)


            #paso los datos a diccionario
            records = {"id":identificacion,
                        "usuario":usuario,
                        "tiempo":tiempo,
                        "monedas":monedas,
                        "rondas":rondas}
            #lo agrego a la lista
            lista_records.append(records)
    return lista_records

def crear_nuevo_record (usuario:str,tiempo:int,monedas:int,rondas:int)-> dict:
    """
    Crea y devuelve un nuevo registro con información del usuario.

    Args:
    usuario (str): El nombre del usuario.
    tiempo (float): El tiempo registrado por el usuario.
    monedas (int): La cantidad de monedas recolectadas por el usuario.
    rondas (int): El número de rondas completadas por el usuario.

    Returns:
    dict: Un diccionario que representa el nuevo registro con las claves 'id', 'usuario', 'tiempo', 'monedas' y 'rondas'.
    """
    nuevo_record = {"id":"",
                "usuario":usuario,
                "tiempo":tiempo,
                "monedas":monedas,
                "rondas":rondas}
    return nuevo_record

def dar_de_alta_nuevo_record(lista_records:list[dict],nuevo_record:dict)->list[dict]:
    """
    Agrega un nuevo record al diccionario de recods existentes con su id correspondiente.

    Args:
        lista_records (list[dict]): La lista de diccionarios que contiene los datos de los records existentes.

    Returns:
        list[dict]: La lista de records actualizada con la nuevo record agregada.
    """
    if lista_records:#si la lista tiene elementos
        identificacion_nuevo_records = lista_records[-1]['id'] + 1 # voy al ultimo elemento de la lista y le sumo 1
    else: # si la lista no tiene elementos significa que es la primera entrada
        identificacion_nuevo_records = 1 #entonces le asigno 1 a la primera pelicula
    
    nuevo_record["id"] = identificacion_nuevo_records #en el diccionario ,en la identificacion lo registro a su id
    lista_records.append(nuevo_record) # y lo agrego a la lista de records
    return lista_records


#queda guardar los datos de nuevos usuario en un diccionario y darlos de alta

#----------Descargar---------
def guardar_actualizacion_csv(lista:list[dict],path:str):

    """
    Guarda la lista actualizada de películas en un archivo CSV en la ruta especificada.

    Args:
        lista (list[dict]): La lista de diccionarios que contiene los datos de las películas.
        path (str): La ruta del archivo CSV donde se guardarán los datos.

    Returns:
        None
    """

    archivo = open(path,"w+",encoding='utf-8')
    archivo.write("ID,Usuario,Tiempo,Monedas,Rondas\n")
    for i in range(len(lista)):
        identificacion = int(lista[i]['id'])
        usuario = lista[i]['usuario']
        tiempo = lista[i]['tiempo']
        monedas = lista[i]['monedas']
        rondas = lista[i]['rondas']


        archivo.write(f'{identificacion},{usuario},{tiempo},{monedas},{rondas}\n')


    archivo.close()

##################  JSON  ##################
import json

path = "logos_path.json"
with open(path, 'r') as f:
    data = json.load(f)
