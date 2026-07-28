from discover import discover

print("=" * 60)
print("Huawei Discovery Tool V2")
print("=" * 60)

ip = input("Switch IP Address : ").strip()
community = input("SNMP Community   : ").strip()

discover(ip, community)

input("\nPress ENTER to Exit...")
