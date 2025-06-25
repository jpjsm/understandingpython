#!/bin/python
import sys
import io
import subprocess
import os
import time
import tempfile


io.DEFAULT_BUFFER_SIZE = 128 * 1024

## Mimicking tempfiles
sbytes = os.urandom(20)
tmpfilename = str.join('-', ["{:02x}".format(ord(c)) for c in sbytes])
stdouttmp = tmpfilename + '.stdout.tmp'
stderrtmp = tmpfilename + '.stderr.tmp'
with io.open(stdouttmp, 'w+t') as localstdout, io.open(stderrtmp, 'w+t') as localstderr:
    ping = subprocess.Popen(['ping', '-c', '2', 'localhost'], stdout=localstdout, stderr=localstderr)
    ping.wait()
    localstdout.seek(0)
    localstderr.seek(0)
    print '[Mimick tempfile] Ping status code: {0}'.format(ping.returncode)
    print '[Mimick tempfile] Ping stdout:\n{0}'.format(localstdout.read(None))
    print '[Mimick tempfile] Ping stderr:\n{0}'.format(localstderr.read(None))

isstdoutdeleted = False
isstderrdeleted = False
attemptsremaining = 3
while attemptsremaining > 0 and not (isstdoutdeleted and isstderrdeleted):
    try:
        if os.path.isfile(stdouttmp):
            os.unlink(stdouttmp)
        isstdoutdeleted = True
    except:
        attemptsremaining -= 1
        time.sleep(1.0)

    try:
        if os.path.isfile(stderrtmp):
            os.unlink(stderrtmp)
        isstderrdeleted = True
    except:
        attemptsremaining -= 1
        time.sleep(1.0)

## using tempfile
with tempfile.TemporaryFile() as localstdout, tempfile.TemporaryFile() as localstderr:
    ping = subprocess.Popen(['ping', '-c', '2', 'localhost'], stdout=localstdout, stderr=localstderr)
    ping.wait()
    localstdout.seek(0)
    localstderr.seek(0)
    print '[Using tempfile] Ping status code: {0}'.format(ping.returncode)
    print '[Using tempfile] Ping stdout:\n{0}'.format(localstdout.read())
    print '[Using tempfile] Ping stderr:\n{0}'.format(localstderr.read())


## using StringIO
with io.StringIO() as localstdout, io.StringIO() as localstderr:
    ping = subprocess.Popen(['ping', '-c', '2', 'localhost'], stdout=localstdout, stderr=localstderr)
    ping.wait()
    localstdout.seek(0)
    localstderr.seek(0)
    print '[Using StringIO] Ping status code: {0}'.format(ping.returncode)
    print '[Using StringIO] Ping stdout:\n{0}'.format(localstdout.read())
    print '[Using StringIO] Ping stderr:\n{0}'.format(localstderr.read())

# sys.stdout = localstdout
# sys.stderr = localstderr

# with io.open('spstdout.txt', 'rt') as localstdout, io.open('spstderr.txt', 'rt') as localstderr:
