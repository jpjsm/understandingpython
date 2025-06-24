#!/usr/bin/env python

# taken from https://docs.python.org/2/howto/argparse.html

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()

print args.echo