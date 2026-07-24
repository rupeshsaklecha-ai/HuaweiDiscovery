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
        return None

    if errorStatus:
        return None

    for name, value in varBinds:
        return str(value)

    return None


def snmp_walk(ip, community, oid):

    data=[]

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
            break

        if errorStatus:
            break

        for name,value in varBinds:

            data.append((str(name),str(value)))

    return data
