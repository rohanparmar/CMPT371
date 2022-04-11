import numpy as np

def readTable():
    tableData = []
    with open("tableInput.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if(line != "\n"):
                tableData.append(line[0:-1].split("\t"))

    return tableData



def andOperator(address, netmask):
    return (bin(address & netmask).replace('b', ''))

def applyMask(address, netmask):
    addressList = address.split('.')
    addressList = list(map(int, addressList))
    netmaskList = netmask.split('.')
    netmaskList = list(map(int, netmaskList))

    outputAddress = []
    for x in range(4):
        outputAddress.append(netmaskList[x] & addressList[x])
    outputAddress = ".".join([str(int) for int in outputAddress])
    return outputAddress

def addressToBinary(address):
    addressBinaryList = []
    for x in range(4):
        addressBinaryList.append(int(address.split('.')[x]))
        addressBinaryList[x] = '{:08b}'.format(addressBinaryList[x])

    return ".".join([str(int) for int in addressBinaryList])

def netmaskInt(netmask): 
    return sum(bin(int(x)).count('1') for x in netmask.split('.'))

def getNetmaskFromRow(row):
    return netmaskInt(row[2])

def sortTable(table):
    return sorted(table, key=getNetmaskFromRow)

def route(address, netmask):
    destination_address = applyMask(address, netmask)
    #Use the metric (metric field - either 1 or 0)
    next_hop_address = '{address}'
    PORT = 3000

    print("\tThe destination IP address is", destination_address)
    print("\tThe next hop IP address is", next_hop_address)
    print("\tThe port the packet will leave through is", PORT)
    print('')

def findRoute(address, routingTable):
    #Search routing table and find best route
    addressBitMask = netmaskInt(address)
    for x in range(len(routingTable)):
        if netmaskInt(routingTable[x][2]) == addressBitMask:
            return routingTable[x][2]

    return 'find route'

def routerStart():
    #Read routing table

    #Put all the rows into a matrix

    #SAMPLE TABLE
   # routingTable = [[ '201.123.32.0', '*', '255.255.254.0', 0, 'eth1' ], [ '201.123.64.0', '123.122.0.2', '255.255.192.0', 1, 'eth2'], [ '123.123.123.123', '123.123.0.2', '255.255.192.0', 0, 'eth3'], [ '123.123.123.123', '*', '255.255.248.0', 0, 'eth4']]
    
    routingTable = readTable()

    #Sort routing table by mask length (netmaskInt(netmask))
#    routingTable = sortTable(routingTable)

    #Print routing table
    print('ROUTING TABLE: ')
    for x in range(len(routingTable)):
        print('\t', routingTable[x])

    print('')
    return routingTable

routingTable = routerStart()
input_address = input("Enter Address: ")
running = True

while running:
    #LOGIC: Read in address, find the right route to send it through, print
    destination_address = findRoute(input_address, routingTable)
    route(input_address, '255.255.255.0')

    close = input("Route another packet? (yes/no) ")
    if(close == "no"):
        running = False
    else:
        input_address = input("Enter Address: ")


