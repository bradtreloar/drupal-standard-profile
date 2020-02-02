#!/usr/bin/env python3

import os
import re
from ruamel.yaml import YAML

sync_dir = "../../../../config/sync"
install_dir = "config/install"

if "install" not in os.listdir("config"):
    os.mkdir(install_dir)

# Delete the existing configuration in this profile.
for filename in os.listdir(install_dir):
    os.remove(os.path.join(install_dir, filename))

# Copy the exported configuration to this profile
for filename in os.listdir(sync_dir):
    # Ignore non-config files.
    if filename in [".htaccess", "README.txt"]:
      continue

    # Load the config file.
    with open(os.path.join(sync_dir, filename), "r") as stream:
        yaml = YAML()
        config = yaml.load(stream)

    # Strip out the _core and uuid entries because these are not allowed
    # in an profile's config.
    if "_core" in config:
        del config["_core"]
    if "uuid" in config:
        del config["uuid"]

    # Save the config file.
    with open(os.path.join(install_dir, filename), "w") as stream:
        yaml.dump(config, stream)
