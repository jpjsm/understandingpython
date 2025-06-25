import fnmatch, os, sys

def cmdfind(path, filter = '*'):
    if not os.path.exists(path):
        return 21, ''

    if os.path.isfile(path):
        return 0, [path]

    filelist = []
    for (top, dirs, files) in os.walk(path):
        filtered = [ f for f in files if fnmatch.fnmatch(f, filter)]
        if filtered:
            filelist += [os.path.join(top, f) for f in filtered]

    return 0, filelist


projectshome = '/Users/jjofre/projects/rba-proxy-seed/overlay/opt/rba-proxy/unit-tests/proxy-api'
status, files = cmdfind(projectshome)
for f in sorted(files,key=str.lower, reverse=True):
    print f
