import os
import nmap
from colorama import Fore, Back, Style, init

init()



print(os.system('pip install python-nmap'))
print(os.system('sudo apt install whois'))
print(os.system('sudo apt install git'))
print(os.system('pip install colorama'))
print("\n\n\n\n\n\n\n\n\n\n")
print(Fore.RED + '                                  ╔╗ ╔╗╔╗ ╔╗     ╔═══╗╔╗ ╔╗╔╗   ╔╗   ')
print(Fore.GREEN + '                                  ║║ ║║║║ ║║     ║╔══╝║║ ║║║║   ║║   ')
print(Fore.BLUE + '                                  ║╚═╝║║╚═╝║     ║╚══╗║║ ║║║║   ║║   ')
print(Fore.YELLOW + '                                  ║╔═╗║╚══╗║     ║╔══╝║║ ║║║║ ╔╗║║ ╔╗')
print(Fore.CYAN + '                                  ║║ ║║   ║║    ╔╝╚╗  ║╚═╝║║╚═╝║║╚═╝║')
print(Fore.RED + '                                  ╚╝ ╚╝   ╚╝    ╚══╝  ╚═══╝╚═══╝╚═══╝')
print(Style.RESET_ALL)                               #Created by Polarized
       
asw = input("\n\n\n\n\n1 - Ports Scanner\n2 - GitHub Cloner(NOT WORKING FOR WINDOWS USERS !)\n3 - Ssh\n4 - Pinger\n5 - Whois Lookup(NOT WORKING FOR WINDOWS USERS !)\n\n\n\n\n\n")
if asw == '1':
    ip = input("\n\n\n\n\nEnter the IP : ")
    print(os.system('nmap ' +ip))  

if asw == '2':
    HOST = input("\n\n\n\n\nEnter the link of the github repository : ")
    print(os.system('git clone' +HOST))

if asw == '3':
   ipp = input("\n\n\n\n\nEnter the IP : ") 
   print(os.system('ssh ' +ipp))

if asw == '4': 
   hostt = input("\n\n\n\n\nEnter the host : ")
   print(os.system('ping ' +hostt))

if asw == '5': 
	A = input("\n\n\n\n\nEnter the host : ")
	print(os.system('whois ' +A))
