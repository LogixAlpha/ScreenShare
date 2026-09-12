import time 
from colorama import Fore , Back , init , Style
import keyboard

# Windows users ONLY 

init(autoreset=True)

print(f"{Back.CYAN}How to use Scrcpy!")
time.sleep(.75)
print(f"{Fore.LIGHTRED_EX}Make sure you ran this script on the scrcpy folder!{Style.RESET_ALL}\n")
print(f"{Fore.RED}1-Verifying Eligibity of your phone.{Style.RESET_ALL}\n"
      f"{Fore.GREEN}2-Setup Scrcpy!{Style.RESET_ALL}\n"
      f"{Fore.LIGHTBLUE_EX}3-Running it Wirelessly!{Style.RESET_ALL}\n"
    )
time.sleep(.6)
o = int(input(f"{Style.BRIGHT}Your option:{Style.RESET_ALL}"))           
if o == 1:
    time.sleep(.5)
    print(f"Running a script ...")
    keyboard.press_and_release('WIN+R')
    keyboard.write("cmd",0.5)
    time.sleep(0.7)
    
