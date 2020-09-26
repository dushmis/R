#!/usr/bin/env python3

from PIL import Image
import argparse
import os
import sys

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dir', type=str, required=True, help='directory to compress it on')
opts = parser.parse_args()

for fname in os.listdir(opts.dir):
  try:
    fname = opts.dir + "/" + fname
    l = Image.open(fname)
    if (l.size[0]>2000) or (l.size[1]>2000):
      newsize = [int(ne / 6) for ne in l.size]
      print("size %s to %s" % (str(newsize),str(l.size)))
      l.resize((newsize[0], newsize[1]), Image.LANCZOS).save(fname)
  except IOError as identifier:
    print(identifier)
