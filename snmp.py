from pysnmp.hlapi import *


def snmp_get(ip, community, oid):

    iterator = getCmd(

        SnmpEngine(),

        CommunityData(community),

        UdpTransportTarget((ip,161), timeout=2, retries=1),

        ContextData(),

        ObjectType(ObjectIdentity(oid))

    )

    errorIndication,errorStatus,errorIndex,varBinds=next(iterator)

    if errorIndication:

        return None

    if errorStatus:

        return None

    for varBind in varBinds:

        return str(varBind[1])



def snmp_walk(ip, community, oid):

    result=[]

    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(

            SnmpEngine(),

            CommunityData(community),

            UdpTransportTarget((ip,161), timeout=2, retries=1),

            ContextData(),

            ObjectType(ObjectIdentity(oid)),

            lexicographicMode=False):

        if errorIndication:

            break

        if errorStatus:

            break

        for varBind in varBinds:

            result.append(

                (

                    str(varBind[0]),

                    str(varBind[1])

                )

            )

    return result


def snmp_test(ip, community):

    value = snmp_get(

        ip,

        community,

        "1.3.6.1.2.1.1.5.0"

    )

    if value is None:

        return False

    return True
