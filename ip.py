import requests
import json
import colorama
import sys,time
import os


from colorama import Fore, Back, Style
colorama.init()
os.system('clear||cls')
time.sleep(0.5)
print(Fore.RED, "         _                           _                         _ ")
print(Fore.BLUE, "        | |__   __ _ ___  __ _ _ __ | |____   ____ _ _ __ ___ | |")
print(Fore.RED, "        | '_ \ / _` / __|/ _` | '_ \| '_ \ \ / / _` | '__/ _ \| |")
print(Fore.BLUE, "        | | | | (_| \__ \ (_| | | | | | | \ V / (_| | | | (_) | |")
print(Fore.RED, "        |_| |_|\__,_|___/\__,_|_| |_|_| |_|\_/ \__,_|_|  \___/|_|")
print("     ")
time.sleep(0.5)
print(Fore.RED , "                                                     @hasanhvarol")
time.sleep(0.5)
url1 = input("Girin: ")
url = "http://ip-api.com/json/{}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query".format(url1)
#url = "http://ip-api.com/json/24.48.0.1"
os.system('clear||cls')

response = requests.get(url).json()
time.sleep(0.5)
print(Fore.RED, "         _                           _                         _ ")
print(Fore.BLUE, "        | |__   __ _ ___  __ _ _ __ | |____   ____ _ _ __ ___ | |")
print(Fore.RED, "        | '_ \ / _` / __|/ _` | '_ \| '_ \ \ / / _` | '__/ _ \| |")
print(Fore.BLUE, "        | | | | (_| \__ \ (_| | | | | | | \ V / (_| | | | (_) | |")
print(Fore.RED, "        |_| |_|\__,_|___/\__,_|_| |_|_| |_|\_/ \__,_|_|  \___/|_|")
print("     ")
time.sleep(0.5)
print(Fore.RED , "                                                     @hasanhvarol")
time.sleep(1)
print(Fore.BLUE, "               Tarama İşlemi Başladı")
time.sleep(1)
print(Fore.RED, "Ip:", response["query"])
time.sleep(2)
print(Fore.BLUE, "Durum:", response["status"])
time.sleep(1)
print(Fore.RED,"Bölge:", response["continent"])
time.sleep(1)
print(Fore.BLUE,"Ülke:", response["country"])
time.sleep(1)
print(Fore.RED,"Ülke Kodu:", response["countryCode"])
time.sleep(1)
print(Fore.BLUE,"Şehir:", response["city"])
time.sleep(1)
print(Fore.RED,"Plaka:", response["region"])
time.sleep(1)
print(Fore.BLUE,"Zaman:", response["timezone"])
time.sleep(1)
print(Fore.RED,"Sağlayıcı:", response["org"])
time.sleep(1)
print(Fore.BLUE,"Zip", response["zip"])
time.sleep(1)
print(Fore.RED,"Proxy:", response["proxy"])

