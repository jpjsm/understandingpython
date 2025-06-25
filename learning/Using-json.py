import json

REGIONS = [
    ['us-tukwila-1', 'r1', 'sea'],
    ['us-phoenix-1', 'r2', 'phx'],
    ['us-ashburn-1', 'us-ashburn-1', 'iad'],
    ['eu-frankfurt-1', 'eu-frankfurt-1', 'fra'],
    ['uk-london-1', 'uk-london-1', 'lon']
]

AP8841 = {
    'manufacturer':'APC',
    'model':'AP8841',
    'ora-part-number':'',
    'default':{
        'ping':True,
        'ports':['20', '21', '22', '23', '80', '161', '161', '443'],
        'access':[('apc','apc','telnet'),('apc','apc','http'),('apc','apc','ssh')]
    }, 
    'compliance':{
        'ping':True,
        'ports':['22'],
        'access':[('apc','apc','ssh')]
    }
}
AP7811B = {
    'manufacturer':'APC',
    'model':'AP8841',
    'ora-part-number':'',
    'default':{
        'ping':True,
        'ports':['20', '21', '22', '23', '80', '161', '161', '443'],
        'access':[('apc','apc','telnet'),('apc','apc','http'),('apc','apc','ssh')]
    }, 
    'compliance':{
        'ping':True,
        'ports':['22'],
        'access':[('apc','apc','ssh')]
    }
}
APC_PDUS = {'AP8841':AP8841, 'AP7811B':AP7811B}
DEVICESDB = {'pdu':{'apc':APC_PDUS, 'sun':[], 'schneider':[]}}

with open('regions.json', 'w') as outfile:
    json.dump(REGIONS, outfile, indent=4, separators=(',', ': '))

with open('devicesdb.json', 'w') as outfile:
    json.dump(DEVICESDB, outfile, indent=4, separators=(',', ': '))

with open('devicesdb.json', 'r') as infile:
    devicesdb = json.load(infile)

print json.dumps(devicesdb, indent=4, separators=(',', ': '))

# reading json generated files
#  Network configuration 
with open('static_mappings-fra.json', 'r') as infile:
    fra = json.load(infile)

routes = len(fra)

for route in fra:
    externalip = route["route"]
    odoproxyaddress = route["ingress"]["next_hop"] 
    odoproxylabel = route["ingress"]["label"] 
    edgeaddress = route["egress"]["next_hop"] 
    edgelabel = route["egress"]["label"] 

'''
# Configure link 0
export link0=ens9
export LocalNetworkAddress=172.24.240.5
export LocalNetworkCIDR=/24
export LocalNetworkGateway=172.24.240.1 

# External IP address
export ExternalIpAddress=38.142.222.60

# Configure gre tunnel
export GreRemote=198.19.128.32
export GreLocal=172.24.240.5
'''

OdoProxySeed={
    'netconfig':{
        'link0':'ens9',
        'LocalNetworkAddress':'172.24.240.5',
        'LocalNetworkCIDR':'/24',
        'LocalNetworkGateway':'172.24.240.1',
        'ExternalIpAddress':'38.142.222.60',
        'GreRemote':'198.19.128.32',
        'GreLocal':'172.24.240.5'
    },
    'nginx':{
        'ExternalIpAddress':'38.142.222.60'
    }
}


with open('odo-proxy-seed.json', 'w') as outfile:
    json.dump(OdoProxySeed, outfile, indent=4, separators=(',', ': '))

