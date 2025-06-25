import difflib, hashlib, os, sys

def getmd5(path):
    md5 = hashlib.md5()
    with open(path, 'rb') as infile:
        md5.update(infile.read())

    return md5.hexdigest()

def MD5FileEqual(FileA, FileB):
    NameA = os.path.basename(FileA)
    NameB = os.path.basename(FileB)
    md5A = getmd5(FileA)
    md5B = getmd5(FileB)
    if md5A != md5B:
        print "{0} != {1} ==> {2} != {3}".format(md5A, md5B, NameA, NameB)
        return False

    return True

def RTrimDiff(FileA, FileB):
    with open(FileA, 'r') as infile:
        aLines = [l.rstrip() for l in infile.readlines()]
    with open(FileB, 'r') as infile:
        bLines = [l.rstrip() for l in infile.readlines()]

    return [ l for l in difflib.unified_diff(aLines, bLines)]


TestFilesLocation = "/Users/jjofre/projects/understandingpython/DiffTests"

if __name__ == '__main__':
    ComparePairs = [
        (os.path.join(TestFilesLocation, 'cert.pem'), os.path.join(TestFilesLocation, 'server.svc1.test.crt')),
        (os.path.join(TestFilesLocation, 'client.pem'), os.path.join(TestFilesLocation, 'clt1.svc1.test.crt')),
        (os.path.join(TestFilesLocation, 'key.pem'), os.path.join(TestFilesLocation, 'server.svc1.test.key'))
    ]
    for a,b in ComparePairs:
        if not MD5FileEqual(a, b):
            lines = RTrimDiff(a,b)
            for line in lines:
                print line
