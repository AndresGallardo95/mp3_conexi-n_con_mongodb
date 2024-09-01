import pymongo
import requests  # Mantenemos la importación en caso de que necesites conectarte a la API nuevamente.

def print_feriados(title, feriados):
    print(f"\n{title}:")
    for feriado in feriados:
        print(f"  - Nombre: {feriado['nombre']}")
        print(f"    Fecha: {feriado['fecha']}")
        print(f"    Tipo: {feriado['tipo']}")
        print(f"    Irrenunciable: {'Sí' if feriado['irrenunciable'] == '1' else 'No'}")
        if feriado['comentarios']:
            print(f"    Comentarios: {feriado['comentarios']}")
        print()  # Línea en blanco entre feriados

def main():
    # Conectar al servidor MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Seleccionar la base de datos "feriados"
    mydb = client['feriados']

    # Seleccionar la colección "feriados2024"
    mycollection = mydb['feriados2024']

    # Código para cargar los datos desde la API (ya ejecutado previamente)
    # Mantén este bloque por si necesitas volver a ejecutar la carga en el futuro.
    # url = "https://apis.digital.gob.cl/fl/feriados/2024"
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    # }
    # response = requests.get(url, headers=headers)
    #
    # if response.status_code == 200:
    #     data = response.json()
    #     if isinstance(data, list):
    #         mycollection.insert_many(data)
    #     else:
    #         mycollection.insert_one(data)
    #     print("Datos insertados correctamente en la colección 'feriados2024' de la base de datos 'feriados'")
    # else:
    #     print(f"Error en la solicitud a la API. Código de estado: {response.status_code}")

    # a. Obtener todos los feriados en la colección
    all_holidays = list(mycollection.find())
    print_feriados("Todos los feriados", all_holidays)

    # b. Obtener solo los feriados de tipo “Religioso”
    religious_holidays = list(mycollection.find({"tipo": "Religioso"}))
    print_feriados("Feriados Religiosos", religious_holidays)

    # c. Obtener solo los feriados que sean irrenunciables
    irrenunciable_holidays = list(mycollection.find({"irrenunciable": "1"}))
    print_feriados("Feriados Irrenunciables", irrenunciable_holidays)

    # d. Obtener solo los feriados que incluyen el texto “Santo” en su nombre
    santo_holidays = list(mycollection.find({"nombre": {"$regex": "Santo", "$options": "i"}}))
    print_feriados("Feriados con 'Santo' en el nombre", santo_holidays)

    # e. Obtener solo los feriados que se celebran entre el 11 de marzo (2024-03-11) y el 31 agosto (2024-08-31)
    date_range_holidays = list(mycollection.find({
        "fecha": {"$gte": "2024-03-11", "$lte": "2024-08-31"}
    }))
    print_feriados("Feriados entre 11 de marzo y 31 de agosto", date_range_holidays)

if __name__ == "__main__":
    main()
