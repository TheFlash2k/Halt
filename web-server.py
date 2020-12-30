from http.server import BaseHTTPRequestHandler,HTTPServer
import os # For changing directory to www/
from logger import LOGGER
from color import Colors

host = "localhost"
port = 8080
current_dir = os.getcwd()
new_dir = './www/'

def init():
    os.chdir(new_dir)
    handle = HTTPServer(
        (host, port), BaseHTTPRequestHandler
    )
    os.chdir(current_dir)
    print(f"{Colors.GREEN}[*]{Colors.RESET} Web Server initialized. WebServer running on {Colors.GREEN}{host}{Colors.RESET}:{Colors.CYAN}{port}{Colors.RESET}")
    LOGGER.log(
        message=f"[INIT] - Server initialized on {LOGGER.getTime()} on {host}:{port}",
        recvfrom="HTTP-WebServer"
    )
    try:
        handle.serve_forever()
    except KeyboardInterrupt:
        print(f"{Colors.RED}[!]{Colors.RESET} Received Termination through {Colors.RED}^C{Colors.RESET}. Exiting...")
        LOGGER.log(
            message=f"[EXIT] - Keyboard Interrupt detected. Closing web server...",
            recvfrom="HTTP-WebServer"
        )
        print(f"{Colors.GREEN}[*]{Colors.RESET} Web Server closed.")
        old_dir = current_dir
    except Exception as E:
        LOGGER.log(
            message= f"{Colors.RED}[ERROR]{Colors.RESET}: {Colors.RED}{E.__class__}{Colors.RESET} occurred.\nDetails: {Colors.RED}{E}{Colors.RESET}",
            recvfrom="HTTP-WebServer",
            log_level=1
        )
        print(f"{Colors.RED}[ERROR]{Colors.RESET} - An error {Colors.GREEN}{E.__class__}{Colors.RESET} occured on WebServer")
    finally:
        handle.server_close()
        exit(0)

if __name__ == '__main__':
    init()
