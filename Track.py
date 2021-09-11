from colorama import Fore
from os import system, name, getenv
from json import loads
from requests import get
from subprocess import check_output


if name == "Aku":
    def clear():
        system("cls")
    system("title Ip Tracker")

else:
    def clear():
        system("clear")

def Track():
    clear()

    ip = input(Fore.GREEN + "Entrez l'ip que vous voulez tracker > ")

    Ip = loads(get("https://api.ipgeolocation.io/ipgeo?apiKey=ea51e6ee9beb47cdad50bec7ab6579d6&ip={ip}").text)

    print()

    for element in Ip:
            print(Fore.BLUE + f"{element} >> {Ip[element]}")

    input(Fore.GREEN + f"\n\nAppuyez sur entrée pour quitter...")
    exit()


def mode():
    debut = input(Fore.CYAN + """
    
  _____               _    
 |_   _| __ __ _  ___| | __
   | || '__/ _` |/ __| |/ /
   | || | | (_| | (__|   < 
   |_||_|  \__,_|\___|_|\_\  Par Aku667
                           
        [1] : Ip tracker


mode >""")
    if debut == "1":
        Track()

while True:
    mode()
    clear()

#merci de pas skid
