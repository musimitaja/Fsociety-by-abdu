import os
import time
import shutil
import subprocess

RED = "\033[31m"
RESET = "\033[0m"

MENU = r"""
███████╗ ███████╗ ██████╗  ██████╗ ██╗███████╗████████╗██╗   ██╗
██╔════╝ ██╔════╝██╔═══██╗██╔════╝ ██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
█████╗   ███████╗██║   ██║██║  ███╗██║█████╗     ██║    ╚████╔╝ 
██╔══╝   ╚════██║██║   ██║██║   ██║██║██╔══╝     ██║     ╚██╔╝  
██║      ███████║╚██████╔╝╚██████╔╝██║███████╗   ██║      ██║   
╚═╝      ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝      ╚═╝   

╔══════════════════════════════════════════════════════════════════════════════╗
║ Fsociety Tool | v1.0.4                                     [ - ] [ □ ] [ X ] ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║ [01] Tool Info              [11] Discord Token Info                         ║
║ [02] IP Info                [12] Discord Token Nuker                        ║
║ [03] DDOS (#soon)           [13] Discord Token Joiner                       ║
║ [04] Mass Report (#soon)    [14] Discord Token BruteForce                   ║
║ [05] Phone Number Lookup    [15] N/A                                       ║
║ [06] Mail Info              [16] Discord Token Generator                    ║
║ [07] Username Tracker       [17] Discord Nitro Generator                    ║
║ [08] SQL Vulnerability      [18] Discord Server Info                        ║
║ [09] Discord Raid           [19] Web Cloner (#soon)                         ║
║ [10] Dmall                  [20] Next Page (1/2) (#soon)                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

ACTIONS = {
    0: "./tools/discord.py",
    1: "./tools/tool_info.py",
    2: "./tools/geoip.py",
    5: "./tools/phone_number.py",
    6: "./tools/mail_info.py",
    7: "./tools/username_tracker.py",
    8: "./tools/sql_vulnerability.py",
    10: "./tools/dmall.py",
    11: "./tools/discord_token_info.py",
    17: "./tools/discord_nitro_generator.py",
    18: "./tools/discord_server_info.py",
    19: "./tools/web_cloner.py",
    20: "./nextpage.py",
}

def clear():
    os.system("clear")

def run_script(path):
    subprocess.run(["python3", path])

def main():
    while True:
        clear()
        print(f"{RED}{MENU}{RESET}")
        try:
            choice = int(input("Choice >> ").strip())
            if choice in ACTIONS:
                run_script(ACTIONS[choice])
            elif choice in [3, 4, 9, 12, 13, 14, 15, 16, 18]:
                print(f"{RED}[!] This option is disabled or unavailable.{RESET}")
                time.sleep(1.5)
            else:
                print(f"{RED}[!] Invalid choice.{RESET}")
                time.sleep(1.5)
        except ValueError:
            print(f"{RED}[!] Please enter a number.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
