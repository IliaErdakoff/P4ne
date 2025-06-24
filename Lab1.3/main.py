import pysnmp
from pysnmp.hlapi import *
from pysnmp.hlapi.v1arch import get_cmd

result =  get_cmd(SnmpEngine(), CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.209", 161)), ContextData(), ObjectType(ObjectIdentity("SNMPv2-MIB", 'sysDescr', 0)))
get_cmd()
for x in result:
    for y in x[3]:
        print(y)

get_cmd(snmpDispatcher=)

