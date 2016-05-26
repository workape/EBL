# EBL
## A collection of scripts to pull in public data and present in EBL format

The EBL (External Block List) capabilities of the Palo Alto Networks firewalls are powerful
and allow for the use of external data sources which have been manipulated into a common
format for ingesting into the firewalls.

More information one how to configure EBL's can be found [Here](https://live.paloaltonetworks.com/t5/Configuration-Articles/How-to-Configure-Dynamic-Block-List-DBL-or-External-Block-List/ta-p/53414 "Guide to EBL on live.paloaltonetworks.com")

## O365-parse.py
This script will ingest data from the Microsoft published XML data for the IPv4 and IPv6 addresses as well as the URL's for Office 365 cloud services.

It will output data lists from each product and type (IPv4, IPv6, URL) into an individual list which can then be addressed in the EBL configuration on the firewall.