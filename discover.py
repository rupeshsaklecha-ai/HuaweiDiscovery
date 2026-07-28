from config import SWITCHES
from snmp import snmp_walk
from oids import IFNAME, ENT_ALIAS


def get_ent_mapping(sw):

    rows = snmp_walk(
        sw["ip"],
        sw["community"],
        ENT_ALIAS
    )

    print("\nENT_ALIAS WALK")
    print("-" * 60)

    for oid, value in rows:
        print("OID  :", oid)
        print("VALUE:", value)
        print()

    return {}


def discover():

    for sw in SWITCHES:

        print("=" * 60)
        print("Switch :", sw["name"])
        print("IP     :", sw["ip"])
        print("=" * 60)

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

        get_ent_mapping(sw)

        print("\nPorts")
        print("-" * 40)

        for oid, value in ports:

            if "XGigabitEthernet" in value:

                idx = oid.split(".")[-1]

                print(f"{value:30} ifIndex={idx}")
