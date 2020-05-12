import pdfkit
import json
import xmltodict
import xml.etree.ElementTree as parse
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

time = datetime.datetime.now()
date = time.year, time.month, time.day, time.hour, time.minute, time.second, time.microsecond

airport_api = "http://amoapi.kma.go.kr/amoApi/metar?icao=RKSI"

waring = "안녕하세요! Metar 자동 프린트 시스템입니다.\n 본 시스템은 항공기상청 API를 이용하여서 불러옵니다."
error_waring = "Error : ICAO Code entered incorrectly | 다시 입력하세요."

# Airport Input ICAO
airport = input("ICAO Code Capital Letter : ")

if (airport == rksi):
    print("RKSI / 인천국제공항")
    print("조회 시간: " + time.localtime(time.time()))
else:
    print(error_waring)    
    exit()