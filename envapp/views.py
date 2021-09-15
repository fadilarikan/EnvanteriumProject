import json

from envapp.models import Count

count_path = ''
def index(request):
    # Opening JSON file
    fileCounts = open('counts.json', )
    dataCounts = json.load(fileCounts)
    fileMaster = open('master.json', )
    dataMaster = json.load(fileMaster)

    """for i in dataCounts:
           for j in i["completedCounts"]:
               for k in j["contents"]:
                   count = Count()
                   count.idLocation = i["id"]
                   count.barcode = k["barcode"]
                   count.locationCode = i["locationCode"]
                   for p in dataMaster:
                       if k["barcode"] == p["barcode"]:
                           count.sku = p["sku"]
                           count.urunAdi = p["urun adi"]
                   count.amount = k["amount"]
                   count.save()"""


    with open('Location-Barcode-Amount Report.txt', 'w') as f:
        f.write("location;barcode;amount \n")
        locationAll = Count.objects.values_list('locationCode')
        locationAll = sorted(set(list(locationAll)))
        locationCodeList= [ ]
        for i in locationAll:
            for j in i:
                locationCodeList.append(j)

        for location in locationCodeList:
            values = Count.objects.filter(locationCode = location).values("barcode","amount")
            for i in values:
                x = location + ";" +i['barcode'] + ";" + str(i['amount']) + '\n'
                f.write(x)

    with open('Barcode-Amount Report.txt', 'w') as f:
        f.write("barcode;amount \n")
        barcodeAll = Count.objects.values_list('barcode')
        barcodeAll = set(list(barcodeAll))
        barcodeList= [ ]
        for i in barcodeAll:
            for j in i:
                barcodeList.append(j)

        for barcode in barcodeList:
            values = Count.objects.filter(barcode = barcode).values("amount")
            amount = 0
            for i in values:
                amount += i['amount']
            x = barcode + ';' + str(amount) + '\n'
            print(x)
            f.write(x)


    with open('Aggregated Report.txt', 'w') as f:
        f.write("location;barcode;amount;sku;urun adi \n")
        values = Count.objects.all().values("locationCode","barcode","amount","sku","urunAdi")
        for i in values:
            x = i['locationCode'] + ';' + i['barcode'] + ';' + str(i['amount']) + ';' + i['sku'] + ';' + i['urunAdi'] + '\n'
            f.write(x)