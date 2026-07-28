from pysnmp.hlapi import *


# -------------------------------------------------------
# SNMP GET
# -------------------------------------------------------

def snmp_get(ip, community, port, oid):

    iterator = getCmd(

        SnmpEngine(),

        CommunityData(community),

        UdpTransportTarget((ip, port), timeout=2, retries=1),

        ContextData(),

        ObjectType(ObjectIdentity(oid))

    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        return None

    if errorStatus:
        return None

    for varBind in varBinds:
        return str(varBind[1])


# -------------------------------------------------------
# SNMP WALK
# -------------------------------------------------------

def snmp_walk(ip, community, port, oid):

    result = []

    for (
        errorIndication,
        errorStatus,
        errorIndex,
        varBinds
    ) in nextCmd(

        SnmpEngine(),

        CommunityData(community),

        UdpTransportTarget((ip, port), timeout=2, retries=1),

        ContextData(),

        ObjectType(ObjectIdentity(oid)),

        lexicographicMode=False

    ):

        if errorIndication:
            print("SNMP Error :", errorIndication)
            break

        if errorStatus:
            print("SNMP Error :", errorStatus.prettyPrint())
            break

        for varBind in varBinds:

            result.append(

                (

                    str(varBind[0]),

                    str(varBind[1])

                )

            )

    return result


# -------------------------------------------------------
# TEST CONNECTION
# -------------------------------------------------------

def snmp_test(ip, community, port):

    value = snmp_get(

        ip,

        community,

        port,

        "1.3.6.1.2.1.1.5.0"

    )

    if value is None:
        return False

    return True
