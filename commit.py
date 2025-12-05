import argparse
import os
import re
import subprocess
import sys

import format

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('filename')
  parser.add_argument('--date')
  parser.add_argument('--author', default='Bradshaw Kids <robertwb+kids@gmail.com>')
  args = parser.parse_args()

  path = args.filename
  with open(path) as fin:
    content = format.format(fin.read())
  basename = re.sub(r' [(]\d+[)]', '', os.path.basename(path)) + '.yaml'
  with open(basename, 'w') as fout:
    fout.write(content)
  subprocess.check_call(['git', 'diff', basename])
  subprocess.check_call(
      ['git', 'commit', basename,
        '--author=' + args.author,
        '--date=' + args.date])
