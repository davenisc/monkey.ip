#python3

import os
from colorama import Back, Fore, init, Style

init()
print(Fore.GREEN+""+Fore.WHITE+"                                       ╱▔▔▔▔▔╲")
print(Fore.GREEN+""+Fore.WHITE+"                                      ╱┈┈╱▔╲╲╲▏")
print(Fore.CYAN+"Version: "+Fore.YELLOW+"1.0"+Fore.GREEN+"             ██ ██████  "+Fore.WHITE+" ╱┈┈╱━╱▔▔▔▔▔╲━╮")
print(Fore.CYAN+"By:"+Fore.YELLOW+"DaveNISC"+Fore.GREEN+"              ██ ██   ██ "+Fore.WHITE+" ▏┈▕┃▕╱▔╲╱▔╲▕╮┃")
print(Fore.CYAN+"Twitter:"+Fore.YELLOW+"@DaveNISC"+Fore.GREEN+"        ██ ██████  "+Fore.WHITE+" ▏┈▕╰━▏▊▕▕▋▕▕━╯")
print(Fore.CYAN+"Web site:"+Fore.YELLOW+"davenisc.com"+Fore.GREEN+"    ██ ██  "+Fore.WHITE+"     ╲┈┈╲╱▔╭╮▔▔┳╲╲")
print(Fore.GREEN+"                         ██ ██ "+Fore.WHITE+"       ╲┈┈▏╭━━━━╯▕▕")
print(Fore.CYAN+"pip install"+Fore.RED+" pydnsbl"+Fore.CYAN+" ________________   "+Fore.WHITE+"╲┈╲▂▂▂▂▂▂╱╱")
print(Fore.YELLOW+"  __  __             _"+Fore.WHITE+"                  ▏┊┈┈┈┈┊┈┈┈╲")
print(Fore.YELLOW+" |  \/  |           | |"+Fore.WHITE+"                 ▏┊┈┈┈┈┊▕╲┈┈╲")
print(Fore.YELLOW+" | \  / | ___  _ __ | | _____ _   _"+Fore.WHITE+"  ╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕")
print(Fore.YELLOW+" | |\/| |/ _ \| '_ \| |/ / _ \ | | |"+Fore.WHITE+" ▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕")
print(Fore.YELLOW+" | |  | | (_) | | | |   <  __/ |_| |"+Fore.WHITE+" ╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲")
print(Fore.YELLOW+" |_|  |_|\___/|_| |_|_|\_\___|\__, |"+Fore.WHITE+"  ╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏")
print(Fore.YELLOW+"                               __/ |"+Fore.WHITE+" ╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔")
print(Fore.YELLOW+"                              |___/"+Fore.WHITE+"  ╲▂▂▂╱┈┈┈┈╲▂▂▂╱")

print()

print("Menu")
print(Fore.RED+"1."+Fore.WHITE+"simple scan")
print(Fore.RED+"2."+Fore.WHITE+"mass scan")

print()
option = int(input(Fore.CYAN+"please choose an option: "))
print(Fore.WHITE+"")
if option == 1:
    os.system('python3 simple.scan.py')
elif option == 2:
    os.system('python3 mass.scan.py')
else:
    print(Fore.GREEN+"wrong option, choose 1 or 2")
