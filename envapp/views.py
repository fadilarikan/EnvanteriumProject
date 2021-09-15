import json

from envapp.models import Count

def index(request):
    # Opening JSON file
    fileCounts = open('counts.json', )
    dataCounts = json.load(fileCounts)
    fileMaster = open('master.json', )
    dataMaster = json.load(fileMaster)

    # Writing data to database
    for data in dataCounts:
           for counts in data["completedCounts"]:
               for value in counts["contents"]:
                   count = Count()
                   count.idLocation = data["id"]
                   count.barcode = value["barcode"]
                   count.locationCode = data["locationCode"]
                   for brc in dataMaster:
                       if value["barcode"] == brc["barcode"]:
                           count.sku = brc["sku"]
                           count.urunAdi = brc["urun adi"]
                   count.amount = value["amount"]
                   count.save()
                   print("The data is written to the database.")
    print("Database writing is complete.")

    # Saving data to Location-Barcode-Amount file
    with open('Location-Barcode-Amount Report.txt', 'w') as f:
        f.write("location;barcode;amount \n")

        # Collecting locationCode and transforming unique location
        locationAll = Count.objects.values_list('locationCode')
        locationAll = sorted(set(list(locationAll)))
        locationCodeList= [ ]
        for loc in locationAll:
            for val in loc:
                locationCodeList.append(val)

        # Writing file process
        for location in locationCodeList:

            #Filtering by product location
            values = Count.objects.filter(locationCode = location).values("barcode","amount")
            for value in values:
                x = location + ";" +value['barcode'] + ";" + str(value['amount']) + '\n'
                f.write(x)
        print("Location-Barcode-Amount Report.txt is complete.")

    # Saving data to Barcode-Amount file
    with open('Barcode-Amount Report.txt', 'w') as f:
        f.write("barcode;amount \n")

        # Collecting barcode and transforming unique barcode
        barcodeAll = Count.objects.values_list('barcode')
        barcodeAll = set(list(barcodeAll))
        barcodeList= [ ]
        for brcs in barcodeAll:
            for brc in brcs:
                barcodeList.append(brc)

        # Writing file process
        for barcode in barcodeList:
            # Filtering by product barcode
            values = Count.objects.filter(barcode = barcode).values("amount")

            # counting amount
            amount = 0
            for quantity in values:
                amount += quantity['amount']
            x = barcode + ';' + str(amount) + '\n'
            f.write(x)
        print("Barcode-Amount Report.txt is complete.")

    # Saving data to Aggregated file
    with open('Aggregated Report.txt', 'w') as f:
        f.write("location;barcode;amount;sku;urun adi \n")

        # Pulling all values(location,barcode,amount,sku,urun adi) in the database
        values = Count.objects.all().values("locationCode","barcode","amount","sku","urunAdi")

        # Writing file process
        for value in values:
            x = value['locationCode'] + ';' + value['barcode'] + ';' + str(value['amount']) + ';' + value['sku'] + ';' + value['urunAdi'] + '\n'
            f.write(x)
        print("Aggregated Report.txt is complete.")