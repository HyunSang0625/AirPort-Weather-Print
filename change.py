import json
import xmltodict
 
with open("RKSI_weather.xml",'r') as f:
    xmlString = f.read()

print(xmlString)
 
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
 
print("API XML File => JSON File Transformation complete")
print(jsonString)
 
with open("RKSI_weather2.json", 'w') as f:
    f.write(jsonString)
    print("JSON File Save Complete !!")
    print(jsonString)

with open("RKSI_weahter2.json") as json_file:
    json_data = json.load(json_file)
    json_main = json_data['response']
    json_body = json_main['body']
    json_items = json_body['items']
    json_item = json_items['item']
    print(json_main)
    print('===========================================================')
    print("Metar Weather")
    weather_metar = json_item['metarMsg']
    print(weather_metar)
    print('===========================================================')