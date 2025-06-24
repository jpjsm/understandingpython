# -*- coding: utf-8 -*-
import os, sys

vipshome = 'C:\\Program Files (x86)\\vips-dev-8.8\\bin'
os.environ['PATH'] = vipshome + ';' + os.environ['PATH']
sys.path.insert(1, vipshome)

import pyvips

SupportedImageFormats = [".bmp", ".csv", ".dz", ".fit", ".fits", ".fts", ".gif", ".hdr", ".heic", ".jpe", ".jpeg", ".jpg", ".mat", ".pbm", ".pfm", ".pgm", ".png", ".ppm", ".tif", ".tiff", ".v", ".vips", ".webp"]
def IsSupportedImageFormat(f):
    return True if os.path.splitext(os.path.basename(f))[1].lower() in SupportedImageFormats else False

def heic2jpeg(sourcefile, destinationfile="", q=100):
    sourcedir, _ = os.path.split(sourcefile)
    if not destinationfile:
        destinationfile, _ = os.path.splitext(os.path.basename(sourcefile))
        destinationfile = os.path.join(sourcedir, destinationfile + '.jpg')

    print(".   loading ... {0}".format(sourcefile))
    image = pyvips.Image.new_from_file(sourcefile, access='sequential', autorotate=True)
    print(".   saving ... {0}".format(destinationfile))
    image.write_to_file(destinationfile, Q=q)

if __name__ == "__main__":
    argscount =  len(sys.argv) -1
    if argscount < 1:
        print("usge: python heic2jpg.py <file-or-folder> [<file-or-folder> ...]")
        sys.exit(1)
    
    for a in sys.argv[1:]:
        if os.path.isfile(a) and os.path.splitext(os.path.basename(a))[1].lower() in [".heic", ".heif"]:
            if IsSupportedImageFormat(a):
                heic2jpeg(a)
            else:
                print("Warning: Ignored unsupported file type for: '{0}'".format(a))
        elif os.path.isdir(a):
            for f in [x for x in os.listdir(a) if os.path.splitext(os.path.basename(x))[1]  in [".heic", ".heif"]]:
                p = os.path.join(a,f)
                heic2jpeg(p)
        else:
            print("Warning: Ignored unmanageable argument: '{0}'".format(a))

    print("successful conversion")
