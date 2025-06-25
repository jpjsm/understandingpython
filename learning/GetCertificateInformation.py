import os, sys, json, datetime, subprocess, tempfile, string, re 

def GetCertInfo(certpath, infotype=''):
    """
    Obtains X509 certificate information

    Params:
    -   certpath: the path to the certificate
    -   infotype: the type of information requested
        -   CN: the Common Name
        -   DC: The list of Domain Components; ie. ['com', 'company', 'service']
        -   DCFULL: The list of Domain Components as a dot separated string; ie. 'service.company.com'
        -   SAN: The list of Subject alternative Names; ie. ['service.company.com', 'service.company.org', 'service.company.net'] 
        -   DNS: Same as SAN
        *   Anything else or empty: The full text of the certificate. This is the default behavior.
    """

    cl = ['openssl', 'x509', '-noout', '-text', '-in', certpath]
    with tempfile.TemporaryFile() as cmd_stdout, tempfile.TemporaryFile() as cmd_stderr:
        rc = subprocess.call(cl, stdout=cmd_stdout, stderr=cmd_stderr, shell=False)
        cmd_stdout.seek(0)
        stdout_buffer = [ line.strip(string.whitespace) for line in cmd_stdout.readlines() ]
        cmd_stderr.seek(0)
        stderr_buffer = [ line.strip(string.whitespace) for line in cmd_stderr.readlines() ]

    if stderr_buffer:
        raise Exception({'stdout_buffer':stdout_buffer, 'stderr_buffer':stderr_buffer, 'errmsg':"\n".join(stderr_buffer)})

    if infotype == 'CN':
        cnpattern = r'^Subject:.+CN=(?P<CN>.*)($|\s)'
        for line in stdout_buffer:
            match = re.search(cnpattern, line)
            if match:
                return match.group('CN')
        return ''

    if infotype == 'DC':
        subjectpattern = r'^Subject:'
        dcpattern = r'DC=(?P<DC>.*?),'
        for line in stdout_buffer:
            if re.search(subjectpattern, line):
                matches = re.findall(dcpattern, line)
                if matches:
                    return matches
        return []

    if infotype == 'DCFULL':
        subjectpattern = r'^Subject:'
        dcpattern = r'DC=(?P<DC>.*?),'
        for line in stdout_buffer:
            if re.search(subjectpattern, line):
                matches = re.findall(dcpattern, line)
                if matches:
                    return '.'.join(reversed(matches))
        return ''

    if (infotype == 'DNS') or (infotype == 'SAN'):
        dnspattern = r'DNS:(?P<DNS>[A-Za-z0-9]+(\.[A-Za-z0-9]+)*)'
        for line in stdout_buffer:
            if re.search(dnspattern, line):
                matches = re.findall(dnspattern, line)
                if matches:
                    return [ m[0] for m in matches ]
        return []

    return stdout_buffer
        


if __name__ == '__main__':
    certshome = "/Users/jjofre/projects/rba-proxy-seed/overlay/opt/rba-proxy/unit-tests/MakeTestCerts/certs"

    signingchain = os.path.join(certshome, "signing-ca-chain.pem")

    svc1svrcertpath = os.path.join(certshome, "svc1/server/server.svc1.test.crt")

    if os.path.exists(svc1svrcertpath):
        print "{0}\nCertificate info for: {1}".format('-'* 72, os.path.basename(svc1svrcertpath))
        print "Cert CN: {0}".format(GetCertInfo(svc1svrcertpath, 'CN'))
        print "Cert Domain Components: {0}".format(GetCertInfo(svc1svrcertpath, 'DC'))
        print "Cert Full Domain component: {0}".format(GetCertInfo(svc1svrcertpath, 'DCFULL'))
        print "Cert DNSs or SANs: {0}".format(GetCertInfo(svc1svrcertpath, 'DNS'))
        


    if os.path.exists(signingchain):
        print "{0}\nCertificate info for: {1}".format('-'* 72, os.path.basename(signingchain))
        print "Cert CN: {0}".format(GetCertInfo(signingchain, 'CN'))
        print "Cert Domain Components: {0}".format(GetCertInfo(signingchain, 'DC'))
        print "Cert Full Domain component: {0}".format(GetCertInfo(signingchain, 'DCFULL'))
        print "Cert DNSs or SANs: {0}".format(GetCertInfo(signingchain, 'DNS'))
