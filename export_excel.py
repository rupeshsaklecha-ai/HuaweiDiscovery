from openpyxl import Workbook


def export_excel(ip, data):

    wb = Workbook()

    ws = wb.active

    ws.title = "Discovery"

    ws.append([
        "Port Name",
        "ifIndex",
        "entPhysicalIndex"
    ])

    for row in data:

        ws.append(row)

    filename = f"HuaweiDiscovery_{ip}.xlsx"

    wb.save(filename)

    print("Saved :", filename)
