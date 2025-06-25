# -*- coding: utf-8 -*-

import os, sys
if __name__ == "__main__":
    argscount =  len(sys.argv) -1
    if argscount < 1:
        print("usge: python ListFilesNotJPG.py <file-or-folder> [<file-or-folder> ...]")
        sys.exit(1)
    
    for a in sys.argv[1:]:
        if os.path.isfile(a) and os.path.splitext(os.path.basename(a))[1] not in [".jpg", ".jpeg"]:
            print("Single file argument: {0}".format(a))
        elif os.path.isdir(a):
            for f in [x for x in os.listdir(a) if os.path.splitext(os.path.basename(x))[1] not in [".jpg", ".jpeg"]]:
                print("File in folder argument: '{0}/{1}' ".format(a, f))
        else:
            print("Warning: Ignored unmanageable argument: '{0}'".format(a))

    print("successful conversion")