import requests

def test_api():
    url = "https://apis.digital.gob.cl/fl/feriados/2024"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica que la solicitud fue exitosa
        print(response.json())  # Imprime la respuesta para verificar que se está recibiendo correctamente
    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a la API: {e}")

if __name__ == "__main__":
    test_api()

