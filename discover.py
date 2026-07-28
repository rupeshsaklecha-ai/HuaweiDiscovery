from snmp import snmp_walk
from export_excel import export_excel
from oids import IFNAME, ENT_ALIAS
from oids import HW_MODEL, HW_SERIAL, HW_SOFTWARE, HW_HARDWARE

model = snmp_get(ip, community, port, HW_MODEL)
serial = snmp_get(ip, community, port, HW_SERIAL)
software = snmp_get(ip, community, port, HW_SOFTWARE)
hardware = snmp_get(ip, community, port, HW_HARDWARE)

def get_ent_mapping(ip, community, port):

    rows = snmp_walk(ip, community,port, ENT_ALIAS)

    mapping = {}

    for oid, value in rows:

        try:

            ifindex = int(value.split(".")[-1])

            ent = int(oid.split(".")[-2])

            mapping[ifindex] = ent

        except:
            pass

    return mapping


def discover(ip, community, port):

    ports = snmp_walk(ip, community,port, IFNAME)

    if len(ports) == 0:

        print("SNMP Failed")
        return

    mapping = get_ent_mapping(ip, community,port,)

    print()
    print("=" * 70)
    print("Port Name".ljust(35), "ifIndex".ljust(10), "entPhysicalIndex")
    print("=" * 70)

    excel_data = []

    for oid, value in ports:

        ifindex = int(oid.split(".")[-1])

        ent = mapping.get(ifindex, "")

        print(value.ljust(35), str(ifindex).ljust(10), ent)

        excel_data.append([value, ifindex, ent])

    export_excel(ip, excel_data)

    print()
    print("Excel Export Completed.")
