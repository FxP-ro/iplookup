import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style

init(autoreset=True)

START_COLOR = (144, 238, 144) 
END_COLOR = (0, 100, 0)     

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, start_color, end_color):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color
    length = len(text)

    for i, char in enumerate(text):
        ratio = i / max(1, length - 1)
        r = int(start_r + (end_r - start_r) * ratio)
        g = int(start_g + (end_g - start_g) * ratio)
        b = int(start_b + (end_b - start_b) * ratio)
        print(f"{rgb_to_ansi(r, g, b)}{char}", end="")
        time.sleep(0.01)
    print(Style.RESET_ALL)

def input_gradient(prompt_text, start_color, end_color):
    gradient_text(prompt_text, start_color, end_color)
    return input("")

def afficher_dessin():
    ascii_art = """

                :::::::::: :::    :::  :::::::::
                :+:        :+:    :+:  :+:    :+:
                +:+         +:+  +:+   +:+    +:+
                :#::+::#     +#++:+    +#++:++#+
          +#+         +#+  +#+   +#+
          #+#        #+#    #+#  #+#
          ###        ###    ###  ###

              | By FxP | GitHub : https://github.com/FxP-ro | Premium : https://fxp.mysellauth.com/ |
       
    """
    lines = ascii_art.splitlines()
    max_length = max(len(line) for line in lines)
    for line in lines:
        print(' ' * ((max_length - len(line)) // 2), end='')
        gradient_text(line, START_COLOR, END_COLOR)

def afficher_menu():
    gradient_text("| Free Version |", START_COLOR, END_COLOR)
    gradient_text("[1] IP Lookup", START_COLOR, END_COLOR)
    gradient_text("[0] Leave", START_COLOR, END_COLOR)

def ip_lookup(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()

        gradient_text(f"IP : {data.get('ip')}\n", START_COLOR, END_COLOR)
        gradient_text(f"City : {data.get('city')}\n", START_COLOR, END_COLOR)
        gradient_text(f"Region : {data.get('region')}\n", START_COLOR, END_COLOR)
        gradient_text(f"Country : {data.get('country')}\n", START_COLOR, END_COLOR)

        location = data.get("loc", "0,0")
        gradient_text(f"Contact details : {location}\n", START_COLOR, END_COLOR)



    except Exception as e:
        print(Fore.RED + f"[!] Error : {e}")

def main():
    while True:
        clear_screen()
        afficher_dessin()
        afficher_menu()
    
        choix = input_gradient("[/] Choose Option :", START_COLOR, END_COLOR)
        clear_screen()

        if choix == '1':
            # IP Lookup
            ip_address = input_gradient("Enter IP : ", START_COLOR, END_COLOR)
            clear_screen()
            afficher_dessin()
            ip_lookup(ip_address)
        else:
            print(Fore.RED + "[!] Invalid Option")

        input_gradient("Press Enter to continue...", START_COLOR, END_COLOR)

if __name__ == "__main__":
    main()
