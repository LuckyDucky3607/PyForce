import sys
import subprocess
from subprocess import PIPE

class Make:
    @staticmethod
    def config_multiple_tor_proxies(proxy_number: int):
        num_sock = 9051
        num_control = 9052 + proxy_number
        is_termux = False

        # Check if running on Termux
        if 'termux' in sys.prefix:
            is_termux = True

        for i in range(proxy_number):
            num_sock += 1
            num_control += 1
            print(f"[*] Configuring TOR on port {num_sock}")

            if is_termux:
                subprocess.run(['cp', '/data/data/com.termux/files/usr/etc/tor/torrc_for_PyForce', f'/data/data/com.termux/files/usr/etc/tor/torrc{i}'], check=True)
                subprocess.run(['mkdir', f'/data/data/com.termux/files/usr/var/lib/tor{i}'], stdout=PIPE, stderr=PIPE, check=True)
                with open(f'/data/data/com.termux/files/usr/etc/tor/torrc{i}', 'a') as tor:
                    tor.write(f'SocksPort {num_sock}\n')
                    tor.write(f'ControlPort {num_control}\n')
                    tor.write(f'DataDirectory /data/data/com.termux/files/usr/var/lib/tor{i}')
                tor = subprocess.Popen(['tor', '-f', f'/data/data/com.termux/files/usr/etc/tor/torrc{i}'], stdout=PIPE)
            else:
                subprocess.run(['cp', '/etc/tor/torrc_for_PyForce', f'/etc/tor/torrc{i}'], check=True)
                subprocess.run(['mkdir', f'/var/lib/tor{i}'], stdout=PIPE, stderr=PIPE, check=True)
                with open(f'/etc/tor/torrc{i}', 'a') as tor:
                    tor.write(f'SocksPort {num_sock}\n')
                    tor.write(f'ControlPort {num_control}\n')
                    tor.write(f'DataDirectory /var/lib/tor{i}')
                tor = subprocess.Popen(['tor', '-f', f'/etc/tor/torrc{i}'], stdout=PIPE)

            for line in tor.stdout:
                if "Bootstrapped 100%" in line.decode("utf-8"):
                    break

            print('[+] Done\n\n')
