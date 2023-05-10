# Written by JadaDev
import requests
import threading
from termcolor import colored
import time
import os

def check_proxy(proxy, checked_proxies, working_proxies, url, timeout):
    try:
        response = requests.get(url, proxies={'http':proxy, 'https':proxy}, timeout=timeout)
        if response.status_code == 200:
            working_proxies.append(proxy)
            print(colored(f'[+] Total Checked: {len(checked_proxies): <10} Total Working: {len(working_proxies): <10} Total Proxies: {len(proxies): <10} {proxy}', 'green'))
            with open('proxy.txt', 'a') as f:
                f.write(proxy + '\n')
        else:
            print(colored(f'[-] Total Checked: {len(checked_proxies): <10} Total Working: {len(working_proxies): <10} Total Proxies: {len(proxies): <10} {proxy}', 'red'))
    except:
        print(colored(f'[-] Total Checked: {len(checked_proxies): <10} Total Working: {len(working_proxies): <10} Total Proxies: {len(proxies): <10} {proxy}', 'red'))
    checked_proxies.append(proxy)


def main():
    global proxies
    print('''
     ██╗ █████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗██╗   ██╗
     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗ ██╔╝
     ██║███████║██║  ██║███████║██████╔╝ ╚███╔╝  ╚████╔╝ 
██   ██║██╔══██║██║  ██║██╔══██║██╔═══╝  ██╔██╗   ╚██╔╝  
╚█████╔╝██║  ██║██████╔╝██║  ██║██║     ██╔╝ ██╗   ██║   
 ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   
    ''')
    url_test = 'http://67.227.23.230'
    url_choice = input("Enter the URL of the proxies list: ") or 'https://raw.githubusercontent.com/JadaDev/proxylist/main/WorkingProxies.txt'
    timeout = input("Enter the timeout in seconds (default is 30, minimum is 1, maximum is 60): ") or '30'
    timeout = int(timeout) if timeout.isdigit() and 1 <= int(timeout) <= 60 else 30
    proxies = requests.get(url_choice).text.strip().split('\n')
    total_proxies = len(proxies)
    print(f'Total Proxies: {total_proxies: <2} Checking Started...')
    checked_proxies = []
    working_proxies = []
    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy, checked_proxies, working_proxies, url_test, timeout))
        t.start()
        time.sleep(0.5)
    while threading.active_count() > 1:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print('\nExiting...')
            os._exit(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Total Proxies: {total_proxies: <2} Total Checked: {len(checked_proxies): <2} Total Working: {len(working_proxies): <2}')
    print('Done!')

if __name__ == '__main__':
    print('''
     ██╗ █████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗██╗   ██╗
     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗ ██╔╝
     ██║███████║██║  ██║███████║██████╔╝ ╚███╔╝  ╚████╔╝ 
██   ██║██╔══██║██║  ██║██╔══██║██╔═══╝  ██╔██╗   ╚██╔╝  
╚█████╔╝██║  ██║██████╔╝██║  ██║██║     ██╔╝ ██╗   ██║   
 ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   
    ''')
    print('           Start JADA PROXY Checker : 1')
    print('           Exit                     : 0')
    print('           Hit Enter')
    while True:
        choice = input()
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            break
        elif choice == '0':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Press 1 to start, 0 to exit.')
