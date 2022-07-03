import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier, geodata
from opencage.geocoder import OpenCageGeocode


number = "+447525139105"
apikey = "91ccf6d87efb4737ac6ffc0bd93445ae"

def get_location_details(urlocation):
    ro_number = phonenumbers.parse("+40721234567", "RO")
    print(carrier.name_for_number(ro_number, "en"))
    geocoder = OpenCageGeocode(apikey)
    query = str(urlocation)
    results = geocoder.geocode(query)
    print(results)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print (lat,lng)
    mymap = folium.Map(location=[lat, lng], zoom_start = 9)
    folium.Marker([lat, lng],popup= urlocation).add_to((mymap))
    mymap.save("Vexlocation.html")

def find_my_son():
    mynumber = phonenumbers.parse(number)
    location = geocoder.description_for_number(mynumber, "en")
    print (location)
    get_location_details(location)
    return location



if __name__ == '__main__':
    find_my_son()


