from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import time

public_ip_request = requests.get('https://api.ipify.org?format=json', timeout=5)
public_ip = public_ip_request.json()['ip']
print(f'Publikus IP cím: {public_ip}')

with open('address.txt', 'r') as file:
    local_ip = file.read().strip()
    print(f'Helyi IP cím: {local_ip}\n')

if public_ip:
    location_data_request = requests.get(f'http://ip-api.com/json/{public_ip}', timeout=5)
    location_data = location_data_request.json()
        
    if location_data.get('status') == 'success':
        print(f'Helyadatok a publikus IP cím alapján:')
        print(f"  Város: {location_data.get('city', 'N/A')}")
        print(f"  Régió: {location_data.get('regionName', 'N/A')}")
        print(f"  Ország: {location_data.get('country', 'N/A')}")
        print(f"  Koordináták: {location_data.get('lat', 'N/A')}, {location_data.get('lon', 'N/A')}")
        print(f"  ISP: {location_data.get('isp', 'N/A')}\n")
    else:
        print(f"Hiba az IP lekéréskor: {location_data.get('message', 'Ismeretlen hiba')}\n")
else:
    print('Nem sikerült lekérni a publikus IP címet.\n')
    
geolocator = Nominatim(user_agent="Helykereso")

varos = input('Add meg a város nevét: ')
location = geolocator.geocode(f"{varos}, Hungary", timeout=10)
if location:
    print(f'\nTalált cím: {location.address}')
    print(f'Koordináták: {location.latitude}, {location.longitude}')
    print(f'Raw adatok: {location.raw}\n')
else:
    print(f'\nNem található ilyen település: {varos}\n')

kiindulópont = (46.072046, 18.231495)
kiinduloponneve = 'Pécs'

célpont = geolocator.geocode("Kaposvár, Hungary", timeout=10)
    
if célpont:
    célpontneve = 'Kaposvár'
    különbség = geodesic(kiindulópont, (célpont.latitude, célpont.longitude)).km
    print(f'{kiinduloponneve} és {célpontneve} közötti távolság: {különbség:.2f} km légvonalban.')
else:
    print('Nem sikerült megtalálni Kaposvárt.')