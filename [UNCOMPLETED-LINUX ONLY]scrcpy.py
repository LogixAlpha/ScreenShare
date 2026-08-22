import time 
from colorama import Fore , Back , init , Style
import keyboard
import os
# LINUX ONLY 

init(autoreset=True)
if os.geteuid() == 0 and "SUDO_USER" in os.environ:
    print(f"Launched via sudo by user: {os.environ['SUDO_USER']}")
    print(f"{Back.CYAN}How to use Scrcpy!")
    time.sleep(.75)
    os = input("What OS do you use? [Windows , Linux]:").strip().lower()
    time.sleep(.4)
    print(f"{Fore.RED}1-Verifying Eligibity of your phone.{Style.RESET_ALL}\n"
                f"{Fore.GREEN}2-Setup Scrcpy!{Style.RESET_ALL}\n"
                f"{Fore.LIGHTBLUE_EX}3-Running it Wirelessly!{Style.RESET_ALL}\n"
    )
    time.sleep(.6)
    o = int(input(f"{Style.BRIGHT}Your option:{Style.RESET_ALL}"))           
    if o == 1:
        time.sleep(.5)
        print(f"Running a script ...")
        keyboard.press_and_release('CTRL+T')
else :
    print("Not a root")
