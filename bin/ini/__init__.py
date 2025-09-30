#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """{f}
Usage:
  {f} <m3u>
  {f} (-h | --help)

Options:
  -h --help  Show this screen.
""".format(f=__file__)

from docopt import docopt
from pathlib import Path
import os
import re
import subprocess
import sys


def main(m3u):
  init(m3u)
  sys.exit()


def extract_suffix(path_raw):
  path = path_raw
  suffix = ''
  targets = ['#', '::', '>']
  for i in targets:
    if i not in path_raw:
      pass
    else:
      idx = path_raw.find(i)
      path = path_raw[:idx]
      suffix = path_raw[idx:]
  return path, suffix


def init(m3u):
  midpath = []
  os.chdir(os.path.dirname(os.path.abspath(m3u)))
  txtpath = open(m3u, 'r', encoding='UTF-8')
  txt = txtpath.read().splitlines()
  for i in txt:
    if not i.startswith('#'):
      i_path, i_suf = extract_suffix(i)
      i_home = re.sub(r'^~', str(Path.home()), i_path)
      i_abs = os.path.abspath(i_home)
      midpath.append(i_abs+i_suf)
    else:
      midpath.append(i)
  return midpath


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args['<m3u>'])
