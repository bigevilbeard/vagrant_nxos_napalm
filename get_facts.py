#!/usr/bin/env python

##############################################################
# Introducation to Napalm
# Author: Stuart Clark <stuaclar@cisco.com>
#
# Demo for Devnet Create 2018 - https://github.com/bigevilbeard/napalm_create
##############################################################

from napalm import get_network_driver

driver = get_network_driver('nxos_ssh')
device = driver(hostname='localhost', 
	            username='vagrant', 
	            password='vagrant',
	            optional_args={'port':2222})

device.open()
print 'Napalm Is Running........'
router_dic = device.get_facts()


for i in router_dic:
   if type(router_dic[i]) == list:
     for k in router_dic[i]:
       print "\t -{}".format(k)
   else:
     print "{}: {}".format(i, router_dic[i])


device.close()



