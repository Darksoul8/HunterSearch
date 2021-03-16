import requests
import time
import os

from core.hunter import Hunter
from core.banner import Banner

while True:

    os.system('clear')

    bann = Banner()
    bann.banner()

    print("\033[1;34m[01]\033[m \033[1;97m- Search\033[m")
    print("\033[1;34m[02]\033[m \033[1;97m- Update\033[m")
    print("\033[1;34m[00]\033[m \033[1;97m- Exit\033[m")
    print("\033[1;97m_________________________\n\033[m")

    opt = input("\033[1;97mOption\033[m \033[1;34m➤ \033[m")

    time.sleep(1)

    if (opt == '01' or opt == '1'):

        domain = input(str("\n\033[1;34m [+] \033[m \033[1;97m URL - (exemple.com): \033[m"))

        try:
            obj = Hunter(domain)
            resp = str(obj.search().text)
            end = obj.treatment(resp)

            print('\033[1;97m',end,'\033[m')
            
            new = str(input("\n\033[1;34m Run again (Y/n): \033[m").upper())

            if(new == "N"):
                break 
            else:
                pass


        except:
       
            print("\033[1;31m Error occured \033[m")

    elif(opt == '2' or opt == '02'):
        os.system("bash core/update.sh")
        print('\n\033[1;97m System Update...\033[m')
        time.sleep(2)
        quit()
    
    elif(opt == '0' or opt == '00'):
        print("\033[1;33m\n    Exiting... \033[m")
        time.sleep(1)
        exit() 

    else:
        print("\033[1;31m\n    -Invalid Option- \033[m")
        time.sleep(2)
        os.system('clear')

