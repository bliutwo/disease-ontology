# Filename: call_google_kr.py
# Description: This will call Google's Knowledge Graph Search API, returning
#              data on the disease.

import sys
sys.dont_write_bytecode = True

import os

"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib

import time

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE

    api_key = open('/home/bliutwo/Dropbox/.api_key').read()
    query = 'arthritis'
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 10,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())
#    print response
#    for i in response:
#        print i, response[i]
#        print
#    print type(response)
    for element in response['itemListElement']:
        print element['result']['name'] + ' (' + str(element['resultScore']) + ')'


    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
#    print t
#    fo = open("results.txt", "wb")
#    fo.write("%d\n%.8f\n" % (t, sumtime))
#    fo.close()


if __name__ == "__main__":
    main()
