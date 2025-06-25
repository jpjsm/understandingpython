"""read python logging config file.

Note:
    - Either have an appconfig.ini file created or
      generate one with write_config.py
"""

import configparser

config = configparser.ConfigParser()
config.read_file(open(r"appconfig.ini"))
with open(r"appconfig_2.ini", "w") as outfile:
    for section_ in config.sections():
        outfile.write(f"[{section_}]\n")
        the_section = config[section_]
        for k in the_section:
            v = config[section_][k]
            outfile.write(f"    {k} = {v}\n")
