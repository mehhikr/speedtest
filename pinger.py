import time
from ping3 import ping

def pings():
    ip = input("enter ip to test: ")
    hosts = [ip]
    
    while True:
        for host in hosts:
            responsetime = ping(host)
            if responsetime:
                print(f"{host} Ping: {responsetime*1000:.2f} ms")
            else:
                print(f"{host} Ping: N/A ms")
        time.sleep(1)


pings()
