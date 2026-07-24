from config import SWITCHES
from oids import *
from snmp import *


def discover():

    print("Huawei Discovery")

    for sw in SWITCHES:

        print(sw["name"])

        ports = snmp_walk(
            sw["ip"],
            sw["community"],
            IFNAME
        )

        print(ports)
