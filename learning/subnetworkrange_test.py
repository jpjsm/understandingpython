from subnetworkrange import SubnetworkRange

for a in ["172.24.240.29/24", "172.24.240.29/29", "172.24.240.29/30", "172.24.240.29/31", "172.24.240.29/32" ]:
    ip1 = SubnetworkRange(a)

    print "{0}".format("="*72)
    print "Address", ip1.Address
    print "Range", ip1.Range
    print "Net", ip1.Net
    print "Broadcast", ip1.Broadcast
    print "Lo", ip1.Lo
    print "Hi", ip1.Hi
    print " "