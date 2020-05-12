import pdfkit
import json
import xmltodict
import pandas as  pd
import urllib.request as link
from xml.etree.ElementTree import parse
import os
import datetime

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

waring = "안녕하세요! Metar 자동 프린트 시스템입니다.\n 본 시스템은 항공기상청 API를 이용하여서 불러옵니다."
error_waring = "Error : ICAO Code entered incorrectly | 다시 입력하세요."

airport = input("ICAO Code Capital Letter : ")

if (airport == rksi):
    print("RKSI / 인천국제공항 | 인천광역시 중구 운서동")
    # Inculde API 
    response = link.urlopen(airport_api + rksi).read()
    xmldoc = parse(response)
    root = xmldoc.getroot()
    main_print = root.findtext('metarMsg')
    print(main_print)
    print("Lookup Time(조회시간) : ", date)
else:
    print(error_waring)    
    exit()