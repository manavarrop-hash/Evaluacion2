import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
idioma = "es"
key = "11123d22-e226-4d10-983d-d807c98b14e8"      # API key de Graphhopper

def geocoding (location, key):
    while location == "":
        location = input("Ingrese la ubicación nuevamente: ")
    geocode_url = "https://graphhopper.com/api/1/geocode?" 
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key, "locale":idioma})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country=""
        
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state=""
        
        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        
        print("URL de la API de Geocodificación para " + new_loc + " (Tipo de ubicación: " + value + ")\n" + url)
    else:
        lat="null"
        lng="null"
        new_loc=location
    return json_status,lat,lng,new_loc

while True:
    loc1 = input("Ubicación de inicio (o ingrese 's' / 'salir' para terminar): ")
    if loc1.lower() == "salir" or loc1.lower() == "s":
        print("Saliendo del programa...")
        break
    orig = geocoding(loc1, key)

    loc2 = input("Ubicación de destino (o ingrese 's' / 'salir' para terminar): ")
    if loc2.lower() == "salir" or loc2.lower() == "s":
        print("Saliendo del programa...")
        break
    dest = geocoding(loc2, key)
    
    print("=================================================")
    if orig[0] == 200 and dest[0] == 200:
        op="&point="+str(orig[1])+"%2C"+str(orig[2])
        dp="&point="+str(dest[1])+"%2C"+str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key":key, "locale":idioma}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        print("Estado de la API de Enrutamiento: " + str(paths_status) + "\nURL de la API de Enrutamiento:\n" + paths_url)

        print("=================================================")
        print("Instrucciones de viaje desde " + orig[3] + " hasta " + dest[3])
        print("=================================================")
        if paths_status == 200:
            miles = (paths_data["paths"][0]["distance"])/1000/1.61
            km = (paths_data["paths"][0]["distance"])/1000
            sec = int(paths_data["paths"][0]["time"]/1000%60)
            min = int(paths_data["paths"][0]["time"]/1000/60%60)
            hr = int(paths_data["paths"][0]["time"]/1000/60/60)
            tiempo_minutos = (paths_data["paths"][0]["time"])/1000/60
            print("Distancia recorrida: {0:.2f} millas / {1:.2f} km".format(miles, km))
            print("Duración del viaje: {0:02d}:{1:02d}:{2:02d} ({3:.2f} minutos)".format(hr, min, sec, tiempo_minutos))
            print("=================================================")
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]
                print("{0} ( {1:.2f} km / {2:.2f} millas )".format(path, distance/1000, distance/1000/1.61))
            print("=============================================")