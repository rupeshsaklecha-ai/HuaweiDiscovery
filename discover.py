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
