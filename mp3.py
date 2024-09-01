import pymongo
import requests

def main():
    # Conectar al servidor MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Seleccionar la base de datos "feriados"
    mydb = client['feriados']

    # Seleccionar la colección "feriados2024"
    mycollection = mydb['feriados2024']

    # Hacer la solicitud a la API para obtener los feriados de 2024
    url = "https://apis.digital.gob.cl/fl/feriados/2024"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta en JSON
        data = response.json()
        
        # Insertar los datos en la colección de MongoDB
        if isinstance(data, list):
            mycollection.insert_many(data)
        else:
            mycollection.insert_one(data)
        
        print("Datos insertados correctamente en la colección 'feriados2024' de la base de datos 'feriados'")
    else:
        print(f"Error en la solicitud a la API. Código de estado: {response.status_code}")

if __name__ == "__main__":
    main()
