from subprocess import call, DEVNULL, Popen, PIPE


class Make:
    @staticmethod
    def config_multiple_tor_proxies(proxy_number: int):
        num_sock = 9051
        num_control = 9052 + proxy_number
        for i in range(proxy_number):
            num_sock += 1
            num_control += 1
            print(f"[*] Configuring TOR on port {num_sock}")
            call(f'cp etc/tor/torrc_for_PyForce /etc/tor/torrc{i}', shell=True)
            call(f'mkdir /var/lib/tor{i}', shell=True, stdout=DEVNULL, stderr=DEVNULL)
            with open(f'/etc/tor/torrc{i}', 'a') as tor:
                tor.write(f'SocksPort {num_sock}\n')
                tor.write(f'ControlPort {num_control}\n')
                tor.write(f'DataDirectory /var/lib/tor{i}')
            tor = Popen(f'tor -f /etc/tor/torrc{i}', shell=True, stdout=PIPE)
            for line in tor.stdout:
                # Check if the proxy has been created
                if "Bootstrapped 100%" in line.decode("utf-8"):
                    # Proxy is ready
                    break
            print('[+] Done\n\n')


