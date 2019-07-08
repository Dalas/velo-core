import os
import yaml


DEFAULT_SETTINGS_PATH = '/etc/velocore/settings.yaml'


def load_settings():
    path = os.environ.get('APP_CONFIG', DEFAULT_SETTINGS_PATH)

    with open(path, 'r') as file:
        settings = yaml.safe_load(file)

    return settings
