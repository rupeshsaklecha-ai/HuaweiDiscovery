from config import SWITCHES
from oids import *
from snmp import *

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

        for oid, value in ports:

            if "XGigabitEthernet" in value:

                ifindex = oid.split(".")[-1]

                print(f"{value:30} ifIndex={ifindex}")
