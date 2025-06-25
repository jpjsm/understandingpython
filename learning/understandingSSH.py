import paramiko

## setup SSH 
sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

## setup remote 
address = '192.168.101.103' ## SUN rPDU
usrname = 'jp'
pwd = 'adm1n'
port = 22

'''
address = '193.1.1.101' ## local VM: jpjofre-mac-vm01
usrname = 'jpjofre'
pwd = 'ABCdef123!'
port = 22
'''

cmds = [
    "set pdu_name={0}\n".format('r410-sun2-pdu'),
    "set net_web_version=0\n",
    "set net_snmp_version=0\n",
    "set net_ipv6_enable=Off\n",
    "set syslogserver_enable.1=On\n",
    "exit"
]

## Open conversation
sshclient.connect(address, port=port, username=usrname, password=pwd, allow_agent=False, look_for_keys=False)
sshtransport = sshclient.get_transport()
sshchannel = sshtransport.open_session()
## Send each command separately
for cmd in cmds:
    print "issuing: {0} ...".format(cmd)
    ## stdin, stdout, stderr = sshclient.exec_command(cmd)  ## Standard procedure
    stdin, stdout, stderr = sshclient.exec_command(cmd)  ## testing if works better with Sun rPDU

    ## Get stdout and stderr output
    stdoutdata = stdout.read()
    stderrdata = stderr.read()

    ## do something with the received output
    print "STDOUT: {0}".format(stdoutdata)
    print "STDERR: {0}".format(stderrdata)

## Close conversation
sshclient.close()