import configparser
config = configparser.ConfigParser()

config['APP'] = {
    'CERTS_PATH': './certs/',
    'DATA_PATH': './data/',
    'LOGS_PATH': './logs/',
    'LOGS_FORMATTER': '%(message)s',
    'LOCAL_ISSUES_FILE_SUFFIX': 'issues.json',
    'MAX_RESULTS': '100',
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)

reloaded_config = configparser.ConfigParser()
reloaded_config.read('config.ini')

for _section in reloaded_config.sections():
    print(f"[{_section}]")
    for _key in reloaded_config[_section]:
        _value = reloaded_config[_section][_key]
        print(f"{_key} = {_value}")
