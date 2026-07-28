from config import SWITCHES
from snmp import *
from oids import *

def discover():

    for sw in SWITCHES:

        print("="*60)
        print("Switch :",sw["name"])
        print("IP     :",sw["ip"])
        print("="*60)

        ports=snmp_walk(
            sw["ip"],
            sw["community"],
            IFNAME
        )

        if len(ports)==0:
            print("SNMP Failed")
            continue

        print("SNMP Connected")
        print()

        for oid,value in ports:

            if "XGigabitEthernet" in value:

                idx=oid.split(".")[-1]

                print(value," ifIndex =",idx)

def get_ent_mapping(sw):

    rows = snmp_walk(
        sw["ip"],
        sw["community"],
        ENT_ALIAS
    )

    mapping = {}

    for oid, value in rows:

        # Example value:
        # IF-MIB::ifIndex.30

        if "ifIndex." in value:

            ifindex = int(value.split(".")[-1])

            ent = int(oid.split(".")[-1])

            mapping[ifindex] = ent

    return mapping

mapping = get_ent_mapping(sw)

print("\nEntity Mapping")
print("-" * 40)

for ifindex in sorted(mapping):
    print(f"ifIndex {ifindex} -> entPhysicalIndex {mapping[ifindex]}")
