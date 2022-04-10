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

def route(address, netmask):
    #Implement forwarding algorithm
    destination_address = applyMask(address, netmask)
    #Use the metric (metric field - either 1 or 0)
    next_hop_address = 'address'
    PORT = 3000
    #Output the following
    print("The destination IP address is", destination_address)
    print("The next hop IP address is", next_hop_address)
    print("The port the packet will leave through is", PORT)



def routerStart():
    #Read routing table
    #Sort routing table
    #Print routing table
    running = True
    

routerStart()

input_address = input("Enter Address: ")
running = True

while running:
    route(input_address, '255.255.255.0')
    close = input("Route another packet? (yes/no) ")
    if(close == "no"):
        running = False
    else:
        input_address = input("Enter Address: ")
