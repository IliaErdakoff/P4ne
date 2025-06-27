
import glob, ipaddress, re

list_ipaddress=[]
ipaddress_new=[]
listfiles= glob.glob('*.log')

for file in listfiles:
    with open(file) as f:
        for row in f:
            m = re.search(r"ip address ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", row )
            if m:
                ipaddress_new.append(ipaddress.IPv4Interface(m.group(1,2)))

for ip in ipaddress_new:
    print(ip)

