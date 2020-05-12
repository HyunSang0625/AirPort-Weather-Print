import pdfkit
import json
import xmltodict
import pandas as  pd
import urllib.request as link
import xml.etree.ElementTree as ET 
import os
import datetime
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from pprint import pprint

rksi = "RKSI"
rkss = "RKSS"
rkjb = "RKJB"
rkpc = "RKPC"
rkpk = "RKPK"
rkny = "RKNY"
rknw = "RKNW"
rktu = "RKTU" 
rktn = "RKTN" 
rkth = "RKTH" 
rkjj = "RKJJ" 
rkjb = "RKJB"
rkjy = "RKJY" 
rkpu = "RKPU"
rkps ="RKPS" 
rkjk = "RKJK"

airport_api = "http://amoapi.kma.go.kr/amoApi/metar?icao="
date = datetime.datetime.now()

welecome = "안녕하세요! Metar 자동 프린트 시스템입니다.\n본 시스템은 항공기상청 API를 이용하여서 불러옵니다."
error_waring = "Error : ICAO Code entered incorrectly"

print(welecome)
airport = input("ICAO Code Capital Letter : ")

if (airport == rksi):
    print("RKSI / 인천국제공항 | 인천광역시 중구 운서동")
    # Inculde API 
    api_link = airport_api + rksi
    print("AIRPORT WEATHER API LINK INCLUDE ")
    r = requests.get(api_link)
    root = ET.fromstring(r.text)
    tree = ET.ElementTree(root)
    tree.write("RKSI_weather.xml")
    doc = ET.parse("RKSI_weather.xml")
    print("Save RKSI XML")  
    with open("RKSI_weather.xml","r") as f:
        xmlString = f.read()
    print("XML Input XML to JSON")
    print(xmlString)

    jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
    print("XML => JSON Save")
    json_link = '/Users/parkhyunsang/Documents/Development/Air_Weather_Print/RKSI_weather.json'
    print(json_link)
    
    print("조회 시간 : ", date)
else: 
    print(error_waring)    
    exit("PLZ Return Input")