#!/usr/bin/env python

##############################################################
# Introducation to Napalm
# Author: Stuart Clark <stuaclar@cisco.com>
#
# Demo for Devnet Create 2018 - https://github.com/bigevilbeard/napalm_create
##############################################################

import json
from napalm import get_network_driver

driver = get_network_driver('nxos_ssh')
device = driver(hostname='localhost', 
	            username='vagrant', 
	            password='vagrant',
	            optional_args={'port':2222})

device.open()
print 'Napalm Is Running........'
get_method = dir(device)


# print get_method
print(json.dumps(get_method, sort_keys=True, indent=4))


device.close()