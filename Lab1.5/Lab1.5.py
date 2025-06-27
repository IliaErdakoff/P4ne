import glob
list_ipaddress=[]
listfiles= glob.glob('*.log')

for file in listfiles:
    with open(file) as f:
         for row in f:
             if "ip address" in row:
                if not "guest" in row:
                     if  not "sub" in row:
                        if not "no" in row:
                            list_ipaddress.append(row)
uniq = list(set(list_ipaddress))
sorted(uniq)
for ip_add in uniq:
    print(ip_add.replace("ip address", ""))
