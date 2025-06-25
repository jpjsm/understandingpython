# Description: This script is used to create a config.ini file with the default values for the JIRA API.
import sys
import configparser
config = configparser.ConfigParser()

config['APP'] = {
    'CERTS_PATH': './certs/jira.cec.lab.emc.com.pem',
    'DATA_PATH': './data/',
    'LOGS_PATH': './logs/',
    'LOGS_FORMATTER': '%(message)s',
    'LOCAL_ISSUES_FILE_SUFFIX': 'issues.json',
}

config['JIRA'] = {
    'MAX_RESULTS': '100',
    'JIRA_URL': 'https://jira.cec.lab.emc.com/rest/api/latest/search',
    'JIRA_AUTH': ('svc_npengrbizreport', 'm3Pr?+n4829bi7yQSCTd5*oK'),
    'JIRA_HEADERS': {'Content-Type': 'application/json'},
    'JIRA_PROJECTS': 'APEXCES,APEXR,SAAS,SAASP',
    'JIRA_HEALTH_CHECK': 'https://jira.cec.lab.emc.com/rest/api/latest/mypermissions',
}

config['MONGODB'] = {
    'MONGODB_URL': 'mongodb://oppy:Mars2004-2018@10.227.242.242:27017/',
    'MONGODB_DB_NAME': 'business-reporting',
    'MONGODB_JIRA_ISSUES_COLLECTION': 'jira-issues',
    'MONGODB_SNOW_CHANGES_COLLECTION': 'snow_changes_response',
    'MONGODB_SNOW_INCIDENTS_COLLECTION': 'snow_incidents_response',
}

config['POSTGRES'] = {
    'POSTGRES_HOST': 'oppy-db-01.cec.delllabs.net',
    'POSTGRES_PORT': '5432',
    'POSTGRES_DB_NAME': 'business_reporter',
    'POSTGRES_USER': 'oppy',
    'POSTGRES_USER_PWD': 'Mars2004-2018',
}


config['SNOW'] = {
    'SNOW_URL': 'https://dell.service-now.com',
    'SNOW_AUTH': 'Basic U2VydmljZV9FU0RfQVBFWF9TTk9XX0RhdGFfUmV0cmlldmU6bngyOHRrYTZyMQ==',
    'SNOW_CHANGE_API': '/api/dusal/change_read_api',
    'SNOW_INCIDENT_API': '/api/dusal/incident_read',
    'SNOW_ASSIGN_GROUPS': ["ITENG-ISG-DEVEX", "ITENG-APEX-EE", "ITENG-DTC-APEX-Infrastructure"],
    'SNOW_DEFAULT_ASSIGN_GROUP': 'ITENG-ISG-EE',
}
with open('config.ini', 'w') as configfile:
    config.write(configfile)

reloaded_config = configparser.ConfigParser()
reloaded_config.read('config.ini')

for _section in reloaded_config.sections():
    print(f"[{_section}]")
    for _key in reloaded_config[_section]:
        _value = reloaded_config[_section][_key].encode('utf-8')
        line = r'%s = %s' %  (_key, _value )
        #sys.stdout.buffer.write(line.encode('utf-8'))
        #sys.stdout.write(line)
        print(str.encode(line))
