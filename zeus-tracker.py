#!/usr/bin/env python
import requests

zeus_domain_url = 'https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist'
zeus_ip_url = 'https://zeustracker.abuse.ch/blocklist.php?download=badips'
ebl_dir = 'ebl-out'

zeus_domain_data = [domain for domain in requests.get(zeus_domain_url).content.split('\n') if (not domain.startswith('#') and domain)]
zeus_ip_data = [ip for ip in requests.get(zeus_ip_url).content.split('\n') if (not ip.startswith('#') and ip)]

with open('%s/zeus-domains.ebl' % ebl_dir, 'w') as z_dom:
    z_dom.write('\n'.join(zeus_domain_data))
with open('%s/zeus-ips.ebl' % ebl_dir, 'w') as z_ip:
    z_ip.write('\n'.join(zeus_ip_data))



