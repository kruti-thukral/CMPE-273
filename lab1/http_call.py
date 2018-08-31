import requests
# makes HTTP get request to the specified URL synchronously
for x in range(3):
    r = requests.get('https://webhook.site')
    if (r.status_code == requests.codes.ok):
        print (r.headers['Date'])
    else:
        print (r.status_code)

