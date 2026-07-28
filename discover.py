from config import SWITCHES
from snmp import snmp_walk
from oids import IFNAME, ENT_ALIAS


def get_ent_mapping(sw):

    rows = snmp_walk(
        sw["ip"],
        sw["community"],
        ENT_ALIAS
    )

    mapping = {}

    for oid, value in rows:

        try:
            # VALUE Example:
            # 1.3.6.1.2.1.2.2.1.1.30
            ifindex = int(value.split(".")[-1])

            # OID Example:
            # 1.3.6.1.2.1.47.1.3.2.1.2.67469454.1
            entPhysicalIndex = int(oid.split(".")[-2])

            mapping[ifindex] = entPhysicalIndex

        except:
            pass

    return mapping


def discover():

    for sw in SWITCHES:

        print("=" * 70)
        print("Switch :", sw["name"])
        print("IP     :", sw["ip"])
        print("=" * 70)

        ports = snmp_walk(
            sw["ip"],
            sw["community"],
            IFNAME
        )

        if len(ports) == 0:
            print("SNMP Failed")
            continue

        print("SNMP Connected")
        print()

        mapping = get_ent_mapping(sw)

        print("Port                           ifIndex   entPhysicalIndex")
        print("-" * 70)

        for oid, value in ports:

            "if "XGigabitEthernet" in value:"

                ifindex = int(oid.split(".")[-1])

                ent = mapping.get(ifindex, "Not Found")

                print(f"{value:30} {ifindex:<9} {ent}")
