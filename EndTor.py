import psutil


def end():
    # Get all the running processes
    all_processes = psutil.process_iter()

    # Iterate over the processes and terminate the Tor processes
    for process in all_processes:
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'cmdline'])
            if process_info['name'] == 'tor' and '-f' in process_info['cmdline']:
                process.terminate()
                #print('Terminated TOR process')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle exceptions if any process is not accessible or has terminated
            print("Exception")
            pass
    print("\n")


if __name__ == '__main__':
    end()
