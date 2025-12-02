# import dataclass
import json
import sys
import xml.dom.minidom
import ruyaml as yaml

# https://stackoverflow.com/questions/45004464/yaml-dump-adding-unwanted-newlines-in-multiline-strings/45004775#45004775
yaml.SafeDumper.org_represent_str = yaml.SafeDumper.represent_str

def repr_str(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')
    return dumper.org_represent_str(data)

yaml.add_representer(str, repr_str, Dumper=yaml.SafeDumper)

def format(s):
  content = json.loads(s)
  if 'workspace' in content:
    content['workspace'] = xml.dom.minidom.parseString(content['workspace']).toprettyxml(indent='  ')
  return yaml.safe_dump(content)

if __name__ == '__main__':
  print(format(sys.stdin.read()))
