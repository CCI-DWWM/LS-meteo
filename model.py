from database import get_connection
import requests

def get_city(codePostal):
    db = get_connection()

    mycursor = db.cursor()

    mycursor.execute(f"SELECT nom_de_la_commune FROM code_postal WHERE code_postal = {codePostal}")

    myresult = mycursor.fetchone()[0]

    pos = get_coordonnees(codePostal)
    print(pos)
    meteo = get_meteo(pos[0], pos[1])
    print(f"météo: {meteo}")


    return {"code postal": codePostal,
            "ville": myresult,
            "meteo": meteo}




def get_coordonnees(postal_code, country_code="fr"):
    """
    Utilise Nominatim (OpenStreetMap) pour obtenir la latitude et la longitude d’un code postal.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "postalcode": postal_code,
        "countrycodes": country_code,
        "format": "json",
        "limit": 1,
    }

    headers = {
        "User-Agent": "MyWeatherApp/1.0 (contact@example.com)"  # Nominatim exige un User-Agent
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    else:
        raise ValueError("Impossible de trouver les coordonnées pour ce code postal.")


def get_meteo(latitude, longitude):
    """
    Utilise Open-Meteo pour récupérer la météo actuelle à partir des coordonnées.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m",
        "timezone": "auto"
    }

    response = requests.get(url, params = params)
    if response.status_code == 200:
        data = response.json()["current"]
        return data
    else:
        raise RuntimeError("Erreur lors de l'appel à Open-Meteo.")