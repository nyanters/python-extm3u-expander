#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = """{f}
Usage:
  {f} (-i <app> | --input <m3u>) [-a <app> | --app <app>]
  {f} (-h | --help)

Options:
  -h --help         Show this screen and exit.
  -i --input <m3u>  M3U Path (required)
  -a --app <app>    App name (optional) [default: VLC]
""".format(f=__file__)

from docopt import docopt
from pathlib import Path
from time import sleep
import ini
import os
import platform
import subprocess
import sys


def main(m3u, app):
  check_os()
  play_mid(m3u, app)
  sys.exit()


def check_os():
  if not platform.system() == 'Darwin':
    sys.exit('This script is for macOS only!')
  else:
    pass
  return


def play_mid(m3u, app):
  tmp_m3u = os.path.join(Path.home(), 'Downloads', 'tmp.m3u')
  txt = ini.init(m3u)
  for i in txt:
    with open(tmp_m3u, 'a', encoding='utf-8') as f:
      print(i, file=f)
  cmd = ['open', '-a', app, tmp_m3u]
  subprocess.run(cmd)
  sleep(5)
  os.remove(tmp_m3u)
  return


if __name__ == "__main__":
  args = docopt(__doc__)
  main(args['--input'], args['--app'])
