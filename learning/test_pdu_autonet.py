import json
import sshtunnel
import pdu_utils
import pdu_autonet

region = 'r1'
plan_endpoint = 'autonet-plan.svc.ad1.{}'.format(region)
bastion_endpoint = 'bastion-ad1.r1.oracleiaas.com'

tunnel = sshtunnel.SSHTunnelForwarder(
    bastion_endpoint,
    remote_bind_address=(plan_endpoint, 80)
)

local_plan_port = tunnel.local_bind_port

endpoint = "localhost:{0}".format(local_plan_port) 
pdusfile = "an_pdu.json"
pdus = []

racksfile = "an_rack.json"
racks = []

devicesfile = "an_devices.json"
devices = []

for region in pdu_utils.REGIONS:
    print "getting information for region: {0}".format(region)
    for pdu in pdu_autonet.pdu_getpdus(endpoint,region):
        pdus.append(pdu)
    
    for rack in pdu_autonet.an_getracks(endpoint, region):
        racks.append(rack)
    
    for device in pdu_autonet.an_getdevices(endpoint, region):
        devices.append(device)

print "Total pdus   : {0}".format(len(pdus))
print "Total racks  : {0}".format(len(racks))
print "Total devices: {0}".format(len(devices))

with open(pdusfile, 'w') as outfile:
    json.dump(pdus, outfile, indent=4, separators=(',', ': '))

with open(racksfile, 'w') as outfile:
    json.dump(racks, outfile, indent=4, separators=(',', ': '))

with open(devicesfile, 'w') as outfile:
    json.dump(devices, outfile, indent=4, separators=(',', ': '))
