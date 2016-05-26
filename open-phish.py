#!/usr/bin/env python

import requests

openphish_url = 'https://openphish.com/feed.txt'
ebl_dir = 'ebl-out'
openphish_data = [url.replace('http://', '').replace('https://', '') for url in requests.get(openphish_url).content.split('\n') if url]

with open('%s/openphish.ebl' % ebl_dir, 'w') as op:
    op.write('\n'.join(openphish_data))
