import requests, json
from requests.auth import HTTPBasicAuth, HTTPDigestAuth, HTTPProxyAuth
from requests_oauthlib import OAuth1

auth_objects = {
    'basic': HTTPBasicAuth,
}

'''
    'digest': HTTPDigestAuth,
    'proxy': HTTPProxyAuth,
}
'''

# r = requests.get('https://bitbucket.oci.oraclecorp.com/rest/api/1.0/projects?start=0', auth=('user', 'pass'))

for u in ['jjofre']: #, 'juan.jofre@oracle.com']:
    for p in ['Vitacura#6256']: #, 'MALjpppvsj1011,.','lliassuciTecriti49#)']:
        for a in auth_objects:
            try:
                with requests.Session() as s:
                    r = s.get('https://bitbucket.oci.oraclecorp.com/rest/api/1.0/projects?start=0', auth=auth_objects[a](u,p), allow_redirects=True) #s.get('https://bitbucket.oci.oraclecorp.com/rest/api/1.0/projects?start=0',auth_objects[a](u,p), allow_redirects=True)
                    if int(r.status_code) != 200 or int(r.json()['size']) > 0:
                        print "Response status code: {0} from user/pwd: {1}/{2} using {3}".format(r.status_code, u, p[:3], a)
                        print "Results: {0}".format(r.text)
            except requests.exceptions.RequestException as rex:
                print "Error while trying with user/pwd {0}/{1} := {2}".format(u, p[:3],rex.response)
        

'''
status_code = r.status_code
print "status code: {0}".format(status_code)
data = r.json()
print data['values']
'''