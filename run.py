#!/usr/bin/env python3

from art import *
from colorama import Fore
from random import choice
import os
from sys import exit
import InternetBruteForce


try:
    def print_center(text):
        terminal_width = os.get_terminal_size().columns
        padding = (terminal_width - len(text)) // 2
        print(' ' * padding + text)



    fonts = ['3-d', '3d_diagonal', '4max', '5lineoblique', 'a_zooloo', 'alligator', 'alligator2', 'amc3line', 'amcaaa01', 'amcneko', 'amcslash', 'avatar', 'banner3-d', 'bell', 'big', 'bigchief', 'block2', 'braced', 'bright', 'bulbhead', 'calgphy2', 'chiseled', 'chunky', 'cola', 'contessa', 'crawford', 'cricket', 'cyberlarge', 'cybermedium', 'dancingfont', 'defleppard', 'doom', 'drpepper', 'eftitalic', 'epic', 'fire_font-s', 'fourtops', 'fuzzy', 'georgi16', 'ghost', 'ghoulish', 'glenyn', 'gothic', 'graceful', 'graffiti', 'henry3d', 'isometric1', 'larry3d', 'merlin1', 'modular', 'nancyj', 'nancyj-fancy', 'nscript', 'ogre', 'pepper', 'poison', 'puffy', 'red_phoenix', 'rev', 'rounded', 'rowancap', 'serifcap', 'slant', 'speed', 'swampland', 'tarty1', 'tarty2', 'tarty3', 'tarty4', 'tarty7', 'varsity']
    print('\n')
    print_center(text2art('PyForce', font=choice(fonts)) + '\t\t\nAuthor: LuckyDucky3607\t\tV.0.5')
    print('\n\n\n')
    path = input(f"\n\n{Fore.LIGHTBLACK_EX}[!] Enter the password list path: ")
    print(Fore.RESET)
    if not os.path.exists(path):
        print(f"\n{Fore.RED}[-] Invalid path exiting...{Fore.RESET}")
        exit()


    integer = input(f"\n{Fore.LIGHTBLACK_EX}[!] Enter the number of threads and proxies at the same time you want to use (Default and recommended 25): ")
    print(Fore.RESET)
    if not integer:
        integer = 25
    try:
        integer = int(integer)
    except ValueError:
        print(f"\n{Fore.RED}[-] Invalid number exiting...{Fore.RESET}")
        exit()
    web = input(f"\n{Fore.LIGHTBLACK_EX}[!] Enter the website's form URI (the action of the form): ")
    print(Fore.RESET)
    indicator = input(f"\n{Fore.LIGHTBLACK_EX}[!] Enter the website's indicator of a successful login or an unsuccessful one, type s in the start of the indicator in case if it is indicating a successful login type u in the start if not (without space e.g.: sHoly Moley!): ")
    print(Fore.RESET)
    if not indicator.startswith('u') and not indicator.startswith('s'):
        print(f"\n{Fore.RED}[-] The indicator should start with a u or an s, exiting...")
        exit()
    print(f"\n\n{Fore.LIGHTGREEN_EX}[+] Starting, have a good time PyForcing!{Fore.RESET}\n\n")
    start = InternetBruteForce.Main(path, integer, web, indicator)
    start.main()

except KeyboardInterrupt:
    exit()
finally:
    print(f"\n\n{Fore.LIGHTGREEN_EX}[+] Have a good day!")
