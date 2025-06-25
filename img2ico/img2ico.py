from PIL import Image
from pathlib import Path


def img2ico(path, iconsize=32):
    iconsize = (int(iconsize) // 4) * 4
    if iconsize < 4 or iconsize > 256:
        iconsize = 32
    img = Image.open(path)
    iconpath = Path.joinpath(Path(path).parent, Path(path).stem + ".ico")
    img.save(iconpath, format="ICO", sizes=[(iconsize, iconsize)])


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        img2ico(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        img2ico(sys.argv[1])
    else:
        print("Usage: python img2ico.py <image-filename> [<resolution-pixels>]")
        print("       - image-filename: the image filename used to generate the ico")
        print("       - resolution-pixels: The resolution of the ico image in pixels.")
        print()
        print("Notes:") 
        print("   1.  Valid values: 4 <= resolution-pixels <= 256.")
        print("   2.  Default value: resolution-pixels == 32")
        print("   3.  If 'resolution-pixels' outside valid range, it gets default value without any message.")
