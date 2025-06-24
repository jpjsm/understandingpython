#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageFilter
#Read image
im = Image.open(os.path.expanduser( '/Users/jjofre/Downloads/2019-06 Spectacle Lake/20190608_154628951_iOS.heic' ))
#Display image
im.show()