from pysnmp.hlapi import *

def snmp_get(ip, community, oid):

    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((ip,161), timeout=2, retries=1),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)
        return None

    if errorStatus:
        print(errorStatus.prettyPrint())
        return None

    for name, value in varBinds:
        return str(value)

    return None


def snmp_walk(ip, community, oid):

    result=[]

    iterator = nextCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((ip,161), timeout=2, retries=1),
        ContextData(),
        ObjectType(ObjectIdentity(oid)),
        lexicographicMode=False
    )

    for errorIndication,errorStatus,errorIndex,varBinds in iterator:

        if errorIndication:
            print(errorIndication)
            break

        if errorStatus:
            print(errorStatus.prettyPrint())
            break

        for name,value in varBinds:
            result.append((str(name),str(value)))

    return result
