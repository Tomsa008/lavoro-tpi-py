import json
import pprint

nome_file = "UrbanClimate.json"
NOME_CITTA = "city"
TEMP = "temperature_celsius"
UMIDITA = "humidity_percent"

comfort_accumulato = {} 
comfort_medio_citta = {}

with open(nome_file, "r") as file:
    stringa_json = file.read()
oggetto_python = json.loads(stringa_json)



for diz in oggetto_python:
    city = diz.get(NOME_CITTA)
    temperatura_val = diz.get(TEMP)
    umidita_val = diz.get(UMIDITA)

    comfort_val = temperatura_val - 0.1 * umidita_val

    if city in comfort_accumulato:
        comfort_accumulato[city]['somma_comfort'] += comfort_val
        comfort_accumulato[city]['count'] += 1
    else:
        comfort_accumulato[city] = {
            'somma_comfort': 0.0,
            'count': 1
        }

for city, dati in comfort_accumulato.items():
    count = dati['count']
    
    if count > 0:
        media_comfort = dati['somma_comfort'] / count
        comfort_medio_citta[city] = round(media_comfort, 2)


print("Il comfort medio analizzando le misurazioni fatte in diverse citta dal 1985 al 2025 e':")
pprint.pprint(comfort_medio_citta)