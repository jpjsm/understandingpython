import requests

endpoints = ["http://www.google.com", "http://localhost", "http://localhost:10001"]

for u in endpoints:
    try:
        r = None
        r = requests.get(u)
    except:
        pass
    finally:
        print r.status_code