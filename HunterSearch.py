import requests
import time
import os
#ĐαɾƙSσυʅ

from core.hunter import Hunter
from core.banner import Banner
#ĐαɾƙSσυʅ

__autor__ = "ĐαɾƙSσυʅ"
__license__ = "MIT"
__Version__ = "2.1"

while True:
#banner and options
    os.system('clear')

    bann = Banner()
    bann.banner()

    print("\033[1;34m[01]\033[m \033[1;97m- Search\033[m")
    print("\033[1;34m[02]\033[m \033[1;97m- Update\033[m")
    print("\033[1;34m[00]\033[m \033[1;97m- Exit\033[m")
    print("\033[1;97m_________________________\n\033[m")

    opt = input("\033[1;97mOption\033[m \033[1;34m➤ \033[m\033[1;97m ")

    time.sleep(1)

    if (opt == '01' or opt == '1'):
        #treatment domain
        while True:
            domain = input(str("\n\033[1;34m [+] \033[m \033[1;97m URL - (exemple.com): \033[m\033[1;97m"))
       
            if (domain.find(".") != -1):
                break
            else:
                print("\n\033[1;31m [x] - Incorret format URL! \n\033[1;31m")
                time.sleep(2)
        try:
            obj = Hunter(domain)
            resp = str(obj.search().text)
            end = obj.treatment(resp)

            print("\n\033[1;34m\033[05mSearching...\033[m\033[m")
            time.sleep(3.5)

            print('\n\033[1;32m[*] - Found! \033[m')
            time.sleep(2)

            print('\033[1;97m',end,'\033[m')
            time.sleep(1.5)

            new = str(input("\n\033[1;34m[+]\033[m \033[1;97m- Run again (Y/n): \033[m").upper())

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
        print("\033[1;34m\n    Exiting... \033[m")
        time.sleep(1)
        exit() 

    else:
        print("\033[1;31m\n    -Invalid Option- \033[m")
        time.sleep(2)
        os.system('clear')
                                                                     #ĐαɾƙSσυʅ
print("\033[1;34m\n - Exiting... \033[m\n")
time.sleep(1)
exit()
#by ĐαɾƙSσυʅ

#ĐαɾƙSσυʅ HunterSearch
#HunterSearch Version 2.1