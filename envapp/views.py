import json

from envapp.models import Count

count_path = ''
def index(request):
    # Opening JSON file
    fileCounts = open('counts.json', )
    dataCounts = json.load(fileCounts)
    fileMaster = open('master.json', )
    dataMaster = json.load(fileMaster)
    for i in dataCounts:
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
                count.save()
                
    with open('Barcode-Amount Report.txt', 'w') as f:
        f.write("barcode;amount \n")
        for i in dataCounts:
            for j in i["completedCounts"]:
                for k in j["contents"]:
                    a = Count.objects.filter(barcode = k["barcode"]).values('amount')
                    amount = 0
                    for i in a:
                        amount += i['amount']
                    x = k['barcode'] + ';' + str(amount) + '\n'
                    print(x)
                    f.write(x)
    with open('Location-Barcode-Amount Report.txt', 'w') as f:
        f.write("location;barcode;amount \n")
        for i in dataCounts:
            for j in i["completedCounts"]:
                for k in j["contents"]:
                    a = Count.objects.filter(barcode=k["barcode"]).values('amount')
                    for p in a:
                        x = i['locationCode']+';'+k['barcode'] + ';' + str(p['amount']) + '\n'
                        print(x)
                        f.write(x)

    with open('Aggregated Report.txt', 'w') as f:
        f.write("location;barcode;amount;sku;urun adi \n")
        for i in dataCounts:
            for j in i["completedCounts"]:
                for k in j["contents"]:
                    sku = " "
                    urunAdi = " "
                    for l in dataMaster:
                        if k["barcode"] == l["barcode"]:
                            sku = l["sku"]
                            urunAdi = l["urun adi"]
                    a = Count.objects.filter(barcode=k["barcode"]).values('amount')
                    for p in a:
                        x = i['locationCode']+';'+k['barcode'] + ';' + str(p['amount']) + ';' + sku + ';' + urunAdi +'\n'
                        print(x)
                        f.write(x)

