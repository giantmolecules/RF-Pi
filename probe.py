#!/usr/bin/env python
# import all the needed libraries
import sys
from netaddr import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from subprocess import *
import datetime
import time

# clear the console
call(["clear"])                                           

# set date-time parameters                                                          
today = datetime.date.today()                 
d=today.strftime("%d, %b %Y")
tf=time.strftime(" %H:%M")
t=time.strftime(" %H:%M:%S")

# define variables                                                          
clients = []                          
uni = 0
mach = []
manu =[]

# our packet handler                                                          
def phandle(p):                       
    global uni    
    if p.haslayer(Dot11ProbeReq):                         
        mac = str(p.addr2)
        if p.haslayer(Dot11Elt):                          
            if p.ID == 0: 
                ssid = p.info                             
                if ssid not in clients and ssid != "":
                    clients.append(ssid)          
                    maco = EUI(mac)
            macf = maco.oui.registration().org   
            print len(clients),mac+" ("+macf+") <--Probing--> "+ssid
            if args.log:
                f.write (str(len(clients))+" "+mac+" ("+macf+") //"+" <--Probing--> "+ssid+"\n")
                if mac not in mach:
                            mach.append(mac)
                            uni+=1
                elif mac not in mach:
                            mach.append(mac)
                            uni+=1                           

# our main function             
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='PyRobe Help')
    parser.add_argument('interface', action="store", help="specify interface (ex. mon0)", default=False)
    parser.add_argument("-l","--log", dest="log",action="store_true", help="print log file")
    args = parser.parse_args()
    if args.log:
        f = open("ProbeLog"+str(today)+str(tf)+".txt","w")    
        sniff(iface=args.interface,prn=phandle, store=0)                    
            print ("\n")
            print "Unique MACs: ",uni
        f.write ("\nUnique MACs: "+str(uni))
        f.write ("\nScan performed on: "+str(d)+" at"+str(t))  
        f.close()                                                 
        print "Log successfully written. Exiting!"
    else:
        sniff(iface=args.interface,prn=phandle, store=0)
        print "\nSuccessfully Exited! No log file written."
