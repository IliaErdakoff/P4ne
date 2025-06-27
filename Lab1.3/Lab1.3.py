import asyncio
from pysnmp.hlapi.asyncio import *

async def run():
       # Получение всех интерфейсов из таблицы
    iterator = next_cmd(SnmpEngine(),
                        CommunityData('public'),
                        await UdpTransportTarget.create(('10.31.70.209', 161)),
                        ContextData(),
                        ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')))

    # Прочитываем результат с помощью await
    results = await iterator

    # Распаковываем результаты
    errorIndication, errorStatus, errorIndex, varBinds = results

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
    else:
        for varBind in varBinds:
            oid, val = varBind
            print("%s = %s" % (oid.prettyPrint(), val.prettyPrint()))

asyncio.run(run())

