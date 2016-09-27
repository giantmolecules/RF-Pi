from scapy.all import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
p = GPIO.PWM(14, 100);
p.start(0);
PROBE_REQUEST_TYPE=0
PROBE_REQUEST_SUBTYPE=4

addressAge = 10
pwmValue = 0
deviceList = []
deviceDict = {}
dictLength = 0

def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type==PROBE_REQUEST_TYPE and pkt.subtype == PROBE_REQUEST_SUBTYPE:
            PrintPacket(pkt)

def PrintPacket(pkt):
    print "Probe Request Captured:"
    try:
        extra = pkt.notdecoded
    except:
        extra = None
    if extra!=None:
        signal_strength = -(256-ord(extra[-4:-3]))
    else:
        signal_strength = -100
        print "No signal strength found"    
    print "Target: %s Source: %s SSID: %s RSSi: %d"%(pkt.addr3,pkt.addr2,pkt.getlayer(Dot11ProbeReq).info,signal_strength)
    if pkt.addr2 not in deviceList:
        deviceList.append(pkt.addr2)
    print deviceList
    if pkt.addr2 not in deviceDict:
        deviceDict[pkt.addr2]=time.time()
    for address, timestamp in deviceDict.items():
        if time.time()-timestamp > addressAge:
            del deviceDict[address]
    print len(deviceDict)
    dictLength = len(deviceDict)
    if dictLength > 10:
        dictLength = 10
    pwmValue = (100/10)*dictLength
    p.ChangeDutyCycle(pwmValue)

def main():
    from datetime import datetime
    print "[%s] Starting scan"%time.time()
    print "Scanning for..."
    sniff(iface=sys.argv[1],prn=PacketHandler)
    
if __name__=="__main__":
    main()
