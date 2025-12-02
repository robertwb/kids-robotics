import argparse
import os
import re
import subprocess
import sys

import format

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('filename')
  args = parser.parse_args()

  path = args.filename
  with open(path) as fin:
    content = format.format(fin.read())
  basename = re.sub(r' [(]\d+[)]', '', os.path.basename(path)) + '.yaml'
  with open(basename, 'w') as fout:
    fout.write(content)
  subprocess.check_call(['git', 'commit', basename])
