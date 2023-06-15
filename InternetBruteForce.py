#!/usr/bin/env python3

from threading import Thread
from time import time
from useProxies import UseProxies
from time import sleep

import EndTor
import GetNewIp
import MakeTorProxies



class Main:
    def __init__(self, password_path: str, number_of_proxies_and_threads: int, website_uri: str, indicator: str):
        self.num_of_proxies_and_threads = number_of_proxies_and_threads
        self.website = website_uri
        if indicator.startswith('u'):
            self.result = [indicator[0], indicator[1:]]
        elif indicator.startswith('s'):
            self.result = [indicator[0], indicator[1:]]
        self.tor = MakeTorProxies.Make()
        self.tor.config_multiple_tor_proxies(self.num_of_proxies_and_threads)
        with open(password_path, 'r') as file:
            self.lines = file.readlines()

        self.used = []
        self.t_used = []
        self.unused = []
        self.timeout_dict_1 = {}  # Remove when done with the project ##EXPERMENTAL ##NOT NEEDED
        self.timeout_list = []
        self.run = False
        self.restarting = False
        for x in self.lines:
            self.unused.append(x.strip())

    def main(self):
        self.run = True
        self.t1 = time()
        print('\n')
        try:
            while self.run:
                threads = []
                for i in range(self.num_of_proxies_and_threads):
                    t = Thread(target=self.temp, args=(i,))
                    threads.append(t)
                    t.start()
    
                for t in threads:
                    t.join()
    
            self.reset_everything_and_try_again()


        finally:
            print('\n[*] Closing threads...')
            self.run = False
            print(f"\n[!] Tried {len(self.used)} passwords.\n")
            print(f"[+] Finished requests in {round(time() - self.t1, 2)} seconds\n")
            exit()



    def reset_everything_and_try_again(self):
        if not self.restarting and len(self.timeout_list) >= 10:
            self.restarting = True
            self.run = False
            print(f"\n\n\n[-] Got too many timeouts ({len(self.timeout_list)} restarting TOR and retrying from where we started)\n")
            EndTor.end()
            sleep(2)
            self.tor.config_multiple_tor_proxies(self.num_of_proxies_and_threads)
            self.lines = []
            self.lines = self.unused
            self.timeout_list = []
            self.used = []
            self.restarting = False
            self.main()


    def temp(self, z):
        total_lines = len(self.lines)
        start = z * (total_lines // self.num_of_proxies_and_threads)
        end = (z + 1) * (total_lines // self.num_of_proxies_and_threads)
        start_line = max(1, min(start, total_lines))
        end_line = min(end, total_lines)

        # Adjusting indices to match Python's 0-based indexing
        start_index = start_line - 1
        end_index = end_line

        # Reading lines between start_index and end_index
        selected_lines = self.lines[start_index+1:end_index]
        while self.run:
            for password in selected_lines:
                if len(self.timeout_list) >= 10 or not self.run:
                    self.run = False
                    break
                
                password = password.strip()
                r = UseProxies(self.website, **YOUR_DATA_HERE**,
                               z + 9052)
                try:
                    r.thread(self.result)
                except StopAsyncIteration:
                    self.timeout_dict_1[password] = z + 9052
                    self.timeout_list.append(password)
                    continue
                except OverflowError:
                    EndTor.end()
                    self.timeout_list = []
                    self.timeout_dict_1 = {}
                    self.run = False
                    break
                self.used.append(password)
                self.unused.remove(password)
                print(
                    f"\033[2A\033[K[!] Trying {round(len(self.used) / (time() - self.t1), 3)} request(s) per second\n[!] Finished {len(self.used)}/{total_lines}\n[+] Requested {password} from TOR on port {z + 9052}",
                    end='\r')
                GetNewIp.main(z)


if __name__ == '__main__':
    main = Main('nums.txt', 21, 'https://www.guessthepin.com/prg.php', 'sHoly Moley!')
    main.main()
