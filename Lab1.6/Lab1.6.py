
import glob, ipaddress, re



list_ipaddress=[]
ipaddress_new=[]
listfiles= glob.glob('*.log')

for file in listfiles:
    with open(file) as f:
        for row in f:
            if "ip address" in row:
                list_ipaddress.append(row)
for row in list_ipaddress:
    m = re.search(r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", row )
    if m:
        ip_mask = m.group(1)+"/" +m.group(2)
        ipaddress_new.append(ipaddress.IPv4Interface(ip_mask))
print(ipaddress_new)

