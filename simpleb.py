#!/usr/bin/python3

import base64
import sys
from colorama import Fore, Back, Style, init

init()

print(Fore.CYAN + """


 .d8888b.   d888                          888          888888b.    .d8888b.      d8888  
d88P  Y88b d8888                          888          888  "88b  d88P  Y88b    d8P888  
Y88b.        888                          888          888  .88P  888          d8P 888  
 "Y888b.     888   88888b.d88b.  88888b.  888  .d88b.  8888888K.  888d888b.   d8P  888  
    "Y88b.   888   888 "888 "88b 888 "88b 888 d8P  Y8b 888  "Y88b 888P "Y88b d88   888  
      "888   888   888  888  888 888  888 888 88888888 888    888 888    888 8888888888 
Y88b  d88P   888   888  888  888 888 d88P 888 Y8b.     888   d88P Y88b  d88P       888  
 "Y8888P"  8888888 888  888  888 88888P"  888  "Y8888  8888888P"   "Y8888P"        888  
                                 888
                                 888			by indiozerah 2023
                                 888			Simple Base64.

""" + Fore.RESET)
print(Fore.YELLOW + """
+=====================================================================================+
| 			Modo de uso ./simpleb.py -d hash para decode		      |
| 			            ./simpleb.py -e hash para encode                  |    
+=====================================================================================+
       """ + Fore.RESET)

if len(sys.argv) < 2:
    print("Verifique o modo de uso!")

else:
    if sys.argv[1] == "-d":
        decode = base64.b64decode(sys.argv[2]).decode('utf-8')
        print(f"Mensagem decodificada: {decode}")
    elif sys.argv[1] == "-e":
        encode = base64.b64encode(sys.argv[2].encode('utf-8')).decode('utf-8')
        print(f"Mensagem codificada: {encode}")