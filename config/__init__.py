import os
import yaml


def load_yaml(yaml_file):
    with open(yaml_file) as f:
        return yaml.load(f)

directory = os.path.dirname(os.path.realpath(__file__))
sites = load_yaml(os.path.join(directory, 'sites.yaml'))
accounts = load_yaml(os.path.join(directory, 'accounts.yaml'))