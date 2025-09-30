#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """{f}
Usage:
  {f} (-m <m3u>)
  {f} (-h | --help)

Options:
  -h --help  Show this screen.
  -m <m3u>   M3U Path (required)
""".format(f=__file__)

from docopt import docopt
from pathlib import Path
import ini
import os
import subprocess
import sys


def main(m3u):
  play_mid(m3u)
  sys.exit()


def play_mid(m3u):
  tmp_m3u = os.path.join(Path.home(), 'Downloads', 'tmp.m3u')
  txt = ini.init(m3u)
  for i in txt:
    with open(tmp_m3u, 'a', encoding='utf-8') as f:
      print(i+'\n', file=f)
  cmd = ['mpv', tmp_m3u]
  subprocess.run(cmd)
  os.remove(tmp_m3u)
  return


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args['-m'])
