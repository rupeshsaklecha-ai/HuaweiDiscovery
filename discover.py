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
    
    mapping = {}

    for oid, value in rows:

        # Value Example:
        # IF-MIB::ifIndex.30
        # या
        # iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifIndex.30

        if "ifIndex." in value:

            try:
                ifindex = int(value.split(".")[-1])
                ent = int(oid.split(".")[-1])

                mapping[ifindex] = ent

            except:
                pass

    return mapping


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

        # Get ifIndex -> entPhysicalIndex Mapping
        mapping = get_ent_mapping(sw)

        print("Entity Mapping")
        print("-" * 40)

        if len(mapping) == 0:
            print("No Mapping Found")
        else:
            for ifindex in sorted(mapping):
                print(f"ifIndex {ifindex} -> entPhysicalIndex {mapping[ifindex]}")

        print()
        print("Ports")
        print("-" * 40)

        for oid, value in ports:

            if "XGigabitEthernet" in value:

                idx = int(oid.split(".")[-1])

                if idx in mapping:
                    print(f"{value:30} ifIndex={idx} entPhysicalIndex={mapping[idx]}")
                else:
                    print(f"{value:30} ifIndex={idx} entPhysicalIndex=Not Found")
