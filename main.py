from discover import discover

print("=" * 60)
print("Huawei Discovery Tool V2.0")
print("Developed by Sun Technologies")
print("=" * 60)

ip = input("Switch IP Address : ").strip()

community = input("SNMP Community   : ").strip()

port = input("SNMP Port [161] : ").strip()

if port == "":
    port = 161
else:
    port = int(port)

discover(ip, community, port)

input("\nPress ENTER to Exit...")
