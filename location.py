from geopy.geocoders import Nominatim
from geopy.distance import geodesic


geolocator = Nominatim(user_agent="Helykereso")
location = geolocator.geocode("Barcs, Hungary")

print(f'{location.address} \n')
print(f'{(location.latitude, location.longitude)}\n')
print(f'{location.raw}\n')


kiindulópont = ['46.072046', '18.231495']
kiinduloponneve = 'Pécs'
célpont = geolocator.geocode("46.352821, 17.795034")
célpontneve = 'Kaposvár'



különbség = geodesic((kiindulópont[0], kiindulópont[1]), (célpont.latitude, célpont.longitude)).km

print(f' {kiinduloponneve} és {célpontneve} közötti távolság: {különbség} km Légvonalban.')



