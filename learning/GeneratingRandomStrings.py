import datetime
from socket import gethostname
import hashlib
import base64
import time

region = 'R1'
address = "192.1.1.101"

print "Starting ..."
collisions = {}
for i in range(1024*1024):
    seed = gethostname() + datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S%f') + region + address

    m5 = hashlib.md5()
    m5.update(seed)
    m5d = m5.digest()
    usrnm = "U" + base64.b64encode(m5d,"-_")[0:12]

    s256 = hashlib.sha256()
    s256.update(seed)
    s256d = s256.digest()
    pwd = base64.b64encode(s256d)

    if usrnm not in collisions:
        collisions[usrnm] = 0
    collisions[usrnm] += 1
    ## print "{0} {1} {2}".format(usrnm, m5hx, pwd)

    if i % 1000 == 0:
        print "[{1: 7}] Total buckets: {0}".format(len([collisions[uname] for uname in collisions if collisions[uname] > 1]), i)    
        print "[{1: 7}] Total collisions: {0}".format(sum([collisions[uname] for uname in collisions if collisions[uname] > 1]), i)    
    time.sleep(0.001)

    print "[{1: 7}] Total buckets: {0}".format(len([collisions[uname] for uname in collisions if collisions[uname] > 1]), 1024*1024 - 1)    
    print "[{1: 7}] Total collisions: {0}".format(sum([collisions[uname] for uname in collisions if collisions[uname] > 1]), 1024*1024 - 1)    
