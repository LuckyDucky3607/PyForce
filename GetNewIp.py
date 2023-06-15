import psutil
import signal


def main(num):
    def find_tor_process():
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['name'] == 'tor' and f'/etc/tor/torrc{num}' in proc.info['cmdline']:
                return proc
        return None


    def send_hup_signal(process):
        process.send_signal(signal.SIGHUP)
        # print('sent')


    # Find the Tor process
    tor_process = find_tor_process()

    if tor_process is None:
        pass
    else:
        # Send the HUP signal
        send_hup_signal(tor_process)
