from config import SWITCHES
from snmp import *
from oids import IFNAME

def discover():

    for sw in SWITCHES:

        print(f"\nConnecting : {sw['ip']}")

        ports = snmp_walk(
            sw["ip"],
            sw["community"],
            IFNAME
        )

        if len(ports) == 0:
            print("SNMP Failed")
        else:
            print(f"SNMP OK ({len(ports)} interfaces found)")
