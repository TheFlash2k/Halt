from datetime import datetime
from color import Colors
import os

class LOGGER():
    def get12Hour():
        current_time = datetime.now()
        date_time = str(current_time.strftime("%d/%m/%Y %H:%M")).split() # Returns time and date accurate to the second
        time = datetime.strptime(date_time[1], "%H:%M")
        time = str(time.strftime("%I:%M %p")).split()
        time = ''.join(time[0].split(':')[0]) + time[1]
        return time
    def getTime():
        current_time = datetime.now()
        return str(current_time.strftime("%d-%m-%Y_%H-%M")) # Returns time and date accurate to the minute
    def log(message,recvfrom="", log_level=0):
        dir = 'logs/'
        if not os.path.exists(dir):
            print(f"{Colors.RED}[!]{Colors.RESET} Directory {Colors.CYAN}{dir}{Colors.RESET} doesn't exist. Creating directory...")
            os.mkdir(dir)
            print(f"{Colors.GREEN}[+] Directory {Colors.CYAN}{dir}{Colors.RESET} successfully created.")
        file = ("[ CRITICAL ]-" if log_level else "") + "HALT_LOGS-" + LOGGER.get12Hour() + ".log"
        if log_level:
            print(f"{Colors.RED}[!] CRITICAL ALERT{Colors.RESET}. Exiting...")
        out = dir + file
        handle = open(out, 'a')

        handle.write(f"-- From {recvfrom} --\n{message}\n")
        handle.write("="*50 + '\n')
        handle.close()
        print(f"{Colors.GREEN}[*]{Colors.RESET} Wrote message from {Colors.MAGENTA}{recvfrom}{Colors.RESET} to {Colors.YELLOW}{out}{Colors.RESET}")
