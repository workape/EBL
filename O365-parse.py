#!/usr/bin/env python
import requests
import lxml.etree

'''
    O365-parse.py -- Tighe Schlottog (tschlottog@paloaltonetworks.com)
    A quick script to pull and parse Office365 data into a series of EBL's for use in Palo Alto Networks firewalls.
    If you want to alter the file write targets, change the file open line to target the directory where you would like
    to have the EBL's written.

    Only two variables need to be set:
    o365_url - this is the location of the XML file containing the Office 365 IP/URL information
    ebl_dir - this is the directory that the user would like to write out their
'''

o365_url = 'https://support.content.office.net/en-us/static/O365IPAddresses.xml'
ebl_dir = 'ebl-out'

ms_xml = lxml.etree.fromstring(requests.get(o365_url).content)
o365_data = {}

for product in ms_xml.xpath('//product'):
    o365_data[product.get('name')] = {} if product.get('name') not in o365_data else o365_data[product.get('name')]
    for data in ms_xml.xpath('//product[@name="%s"]/addresslist' % product.get('name')):
        o365_data[product.get('name')][data.get('type')] = [ip_addr.text for ip_addr in ms_xml.xpath('//product[@name="%s"]/addresslist[@type="%s"]/address' % (product.get('name'), data.get('type')))]
        with open('%s/O365-%s-%s.ebl' % (ebl_dir, product.get('name'), data.get('type')), mode='w') as ebl:
            ebl.write('\n'.join(o365_data[product.get('name')][data.get('type')]))
