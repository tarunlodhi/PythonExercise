import csv

with open('data_set/treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {}

    for row in reader:
        key = row[0]
        mydict[key] = row[1]

    # print(mydict)

    sizeOfDi = len(mydict)
    # print(sizeOfDi)
    # print ("The dictionary is of size: " + str(sizeOfDi))

    mydict['205'] = 10
    # print(mydict)

    mydict['999'] = 12
    # print(mydict)

    for i in mydict:
        print(i, mydict[i])

    infile.close()
