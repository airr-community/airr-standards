# imports
import os.path as osp
import yamlordereddictloader
from glob import glob
from yaml import load

# load all the YAML specs
specs_dir = osp.dirname(__file__)
specs_files = glob(osp.join(specs_dir, '*.yaml'))
specs = {}
for yaml_file in specs_files:
    name = osp.splitext(osp.basename(yaml_file))[0]
    with open(yaml_file, 'r') as ip:
        spec_data = load(ip, Loader=yamlordereddictloader.Loader)
    specs[name] = spec_data

# export the specs as top-level module variables
for name in specs.keys():
    globals()[name] = specs[name]

__all__ = list(specs.keys())
