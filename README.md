# Halt
Python3 based Proxy Server capable of intercepting requests and modifying them on the go

- Halt is currently in development.

## Main Features of halt:
```
- User will be able to specify a port and an ip address(default would be 127.0.0.1:8080) on which the proxy server would listen.
- A stealth mode. This will simply just capture packets and display them on the stdout.
- An output mode. This will work with both stealth and intercept mode where we can easily capture packets and store them in a .pcap file
```

## Usage:

```
-h | --help - Printing the help menu
-a <ip address>| --addr <ip address> - The ip address on which the proxy server would be listening
-p <port 1-65535>| --port <port 1-65535> - The port on which the proxy server would be listening
-s | --stealth - Running in stealth mode.
-o <filename> | --output <filename> - The name of the output file
```
