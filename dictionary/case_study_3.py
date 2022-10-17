import csv

with open('data_set/TreeOrdersSubset.csv', mode='r') as infile:
    reader = csv.reader(infile)
    treeOrders = {}
    for row in reader:
        key = row[0]

        if key not in treeOrders:
            treeNum = row[1]
            treeOrders[key] = int(treeNum)

        else:
            treeNum = row[1]
            prev_count = treeOrders[key]
            treeOrders[key] = int(prev_count) + int(treeNum)

infile.close()
print("length of dictionary ", len(treeOrders))

treeOrders10 = {k: v for k, v in treeOrders.items() if v > 10}

print(treeOrders10)
print("length of dictionary ", len(treeOrders10))
