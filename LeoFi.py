#! /usr/bin/env python3

import os
import random
from time import sleep
import signal
import sys

def handler(signum, frame):
    os.system("clear")
    print("Ctrl C Detected Exiting")
    exit()

signal.signal(signal.SIGINT, handler)


os.system("resize -s 43 132 > /dev/null")

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

if not os.path.isfile('office2john.py'):
    os.system("wget https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/run/office2john.py")


if not os.path.isfile ("passwords.txt"):
    os.system("wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-1000000.txt")
    os.system("mv xato-net-10-million-passwords-1000000.txt passwords.txt")
os.system("zenity --title '☢ LeoFi ☢' --info --text 'Please Use This tool for Educational Purpose' --width 400 > /dev/null 2>&1")

#os.system("service apache2 start | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Start apache2 service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
#os.system("service postgresql start | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Start postgresql service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
sleep(1)

os.system("clear")
print("""
████████████████████████████████████████████████████████████████████████
█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█
█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█
█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░███████████░░▄▀░░███
█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░███░░▄▀░░███
█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░███
█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░███░░▄▀░░███
█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░███████████░░▄▀░░███
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░░░▄▀░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████
github:- https://github.com/Hacker2425              Instagram:- https://instagram.com/iamnikhil2459
        ╔──────────────────────────────────────────────╗
        |                  LeoFi                       |
        |             Bruteforcing tool                |
        |          Tool Coded by @Nikhil               | 
        ┖──────────────────────────────────────────────┙
        [1] Bruteforce Zip File              
        [2] BruteForce Rar File
        [3] BruteForce Cap File (Aircrack-ng)       
        [4] BruteForce Office File                     
        [e] Exit                
""")

choice =input("LeoFi==>")

if choice == '1':
    lol =input("Path of Zip file :- ")
    print("Path to zip file :- "+lol)
    
    dictionary_attack ='zip2john '+ lol +'> lol.txt'
    os.system(dictionary_attack)
    dictionary_attack1 = 'john lol.txt --wordlist=passwords.txt'
    os.system(dictionary_attack1)

    os.system("rm lol.txt")


elif choice == '2':
    nikhil =input("Path of rar file :- ")
    print("Path to rar file :- "+nikhil)

    rar = 'rar2john '+ nikhil +'> lol1.txt'
    os.system(rar)
    rar1 = 'john lol1.txt --wordlist=passwords.txt'
    os.system(rar1)
    os.system("rm lol1.txt")

elif choice == '3':
    my =input("Path of Cap File :- ")
    print("Cap File path set to :- "+my)

    cap = 'aircrack-ng -w passwords.txt '+ my +''
    os.system(cap)

elif choice == '4':
    office = input("Path of office File :- ")
    print("Path to office File :- "+office)

    attack = 'python3 office2john.py'+ office +'> attack.txt'
    os.system(attack)
    attack1 = 'python3 office2john.py attack.txt --wordlist=password.txt'
    os.system(attack1)
    os.system("rm attack.txt")

else:
    os.system("clear")
    exit("Thanks For using LeoFi :)")
