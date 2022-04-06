#Read text input
#Sort Rows by mask length
#Print sorted routing table

#For each packet
#Read IP 
#Convert to binary
#Implement the forwarding algorithm


#print(format(255, "b"))

def maskInterpreter(netmask):
    #print(sum(bin(int(x)).count('1') for x in netmask.split('.')))
    #print(format(int(netmask.split('.')[0]), "b"))
    return sum(bin(int(x)).count('1') for x in netmask.split('.'))

    #from stackoverflow: 
    #https://stackoverflow.com/questions/38085571/how-use-netaddr-to-convert-subnet-mask-to-cidr-in-python

#print(maskInterpreter('201.123.32.0'))
print(bin(1001 & 1111).replace('b', ''))

#for each packet:
    #Read IP destination 
    #Convert IP to binary
        #IP_binary = format(int(IP_address.split('.')[0]), "b")
    #Implement forwarding algorithm
        #Do binary addition on destination and mask
            #ie: print(bin(destination & mask).replace('b', ''))
        #Use the metric (metric field - either 1 or 0)

    #Output the following
        #print("The destination IP address is " + destination_address)
        #print("The next hop IP address is " + next_hop_address)
        #print("The port the packet will leave through is " + PORT)

    #After forwarding a packet
        #Ask if the user wishes to forward another packet
        #if no: terminate program
        #if yes
            #Ask for destination IP address of next packet
            #route next packet
            #do the last four steps again