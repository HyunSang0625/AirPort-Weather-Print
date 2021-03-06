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
import win32print
import win32ui
import win32con

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

airport_api_metar = "http://amoapi.kma.go.kr/amoApi/metar?icao="
airport_api_taf = "http://amoapi.kma.go.kr/amoApi/taf?icao="
date = datetime.datetime.now()

welecome = "\n안녕하세요! Metar 자동 프린트 시스템입니다.\n본 시스템은 항공기상청 API를 이용하여서 불러옵니다.\n"
info = "\n==========================================\n개발자 소개\n박현상\nhyun.sang@parkhyunsang.com\nhttp://parkhuyunsang.com\n==========================================\n"
error_waring = "Error : ICAO Code entered incorrectly"

print(welecome + info)
airport = input("ICAO Code Capital Letter : ")

if (airport == rksi):
    print("RKSI / 인천국제공항 | 인천광역시 중구 운서동")
    # Inculde API 
    api_link = airport_api_metar + rksi
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
    print(jsonString)
    with open("RKSI_weather.json", 'w') as f:
        f.write(jsonString)
        print("JSON File Save Complete !!")
        print(jsonString)
    with open("RKSI_weather.json") as json_file:
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
        note_path = "RKSI_weather.txt"
        with open(note_path, "w") as f:
            local_time = "\n조회시간 : ", date
            f.write(weather_metar, local_time)
            print("입력 완료",date)
            print('===========================================================')
    printer = input("Printer Y or N : ")
    if (printer == "Y"):
        print("Wait...")
        INCH = 1440
        
        weather_metar_printer = weather_metar, "\n조회시간 : ", date
        hDC = win32ui.CreateDC ()
        hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
        print("Printing output in progress")
        hDC.StartDoc ("Weather")   # 프린트 작업 문서 이름에 출력
        hDC.StartPage ()
        hDC.SetMapMode (win32con.MM_TWIPS)
        print("Printed Output Completed")
        hDC.DrawText (weather_metar_printer,(0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_LEFT)
        hDC.EndPage ()
        hDC.EndDoc ()
        print("Printed Output Completed")
    if(printer == "N"):
        print("OK Good Bye")
        exit()
else: 
    print(error_waring)    
    exit("PLZ Return Input")

print("조회 시간 : ", date)
