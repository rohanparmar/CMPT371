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

def findRoute(address, routingTable):
    addressBitMask = netmaskInt(address)

    #FIND THE CLOSEST BITMASK MATCH
    #Either find first element 

    #SAMPLE
    return '1.1.1.0'

def route(address, routingTable):
    netmask = findRoute(address, routingTable)
    next_hop_address = applyMask(address, netmask)

    PORT = 3000

    print("\tThe destination IP address is", address)
    print("\tThe next hop IP address is", next_hop_address)
    print("\tThe port the packet will leave through is", PORT)
    print('')

def routerStart():
    #Read routing table

    #Put all the rows into a matrix

    #SAMPLE TABLE
    routingTable = [[ '201.123.32.0', '*', '255.255.254.0', 0, 'eth1' ], 
                    [ '201.123.64.0', '123.122.0.2', '255.255.192.0', 1, 'eth2'],
                    [ '123.123.123.123', '123.123.0.2', '255.255.192.0', 0, 'eth3'], 
                    [ '123.123.123.123', '*', '255.255.248.0', 0, 'eth4'] 
                ]

    routingTable.sort(key=getNetmaskFromRow)

    print('ROUTING TABLE: ')
    for x in range(len(routingTable)):
        print('\t', routingTable[x])
    print('')

    return routingTable

routingTable = routerStart()
input_address = input("Enter Address: ")
running = True

while running:
    route(input_address, routingTable)

    close = input("Route another packet? (yes/no) ")
    if(close == "no"):
        running = False
    else:
        input_address = input("Enter Address: ")



#Read Routing Table
#Sort Routing Table
#When user inputs destination address, send it through route function and print destination