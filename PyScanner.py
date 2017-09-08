import argparse
import socket
import os
import platform

#options -target (ip/hostname) -all(1-65432) -p (single port) -default (wellknown ports)



p = argparse.ArgumentParser()
p.add_argument('-t', '-target', dest="Target_Host", help="Ip address or hostname of target machine", required=True)
p.add_argument("-p","-port", type=int, dest="Target_Port", help="Port number to test on target machine. Defaults to ports 1-1024", default=range(2,1025))
p.add_argument('-P', '-ping', action="store_true", dest="Ping_Host", help="If -P option is used port scanner will ping target host", default=False)
args = p.parse_args()
    
    
    

def Ping_Target(target):
    if platform.system().lower() == "windows":
        os.system("ping -n 2 " + target)
    else:
        os.system("ping -c 2 " + target)  
        
def Scan_Target(target, ports):
    
    
    for port in ports:
        try: 
            socket.setdefaulttimeout(2.0)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target,port))
        except socket.timeout as e:
            print("Port %d is closed or blocked by firewall" % (port))
            s.close()
        except socket.error as e:
            print("I messed up. Error: %s" % (e))
            s.close()
        else:
            print("Port %d is Open!" % (port))
            s.close()
        


#print args.Ping_Host
#print args.Target_Port
Ping_Target(args.Target_Host)
Scan_Target(args.Target_Host, args.Target_Port)



#connect to target and attempt to connect to port, return any errors and inform if port is open.




#If not ran from command line exits and tells to run from shell

