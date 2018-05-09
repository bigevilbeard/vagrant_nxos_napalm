#!/usr/bin/env python

##############################################################
# Introducation to Napalm
# Author: Stuart Clark <stuaclar@cisco.com>
#
# Demo for Devnet Create 2018 - https://github.com/bigevilbeard/napalm_create
##############################################################


from napalm import get_network_driver
import sys


driver = get_network_driver('nxos_ssh')
device = driver(hostname='localhost', 
                username='vagrant', 
                password='vagrant',
                optional_args={'port':2222})


device.open()
print 'Napalm Is Running........'
device.load_merge_candidate(filename='new_loopbacks.cfg')
diffs = device.compare_config()


if len(diffs) > 0:
    print(diffs)

    commit = raw_input("Type COMMIT to commit the configuration or hit ENTER to abort: ")
    if commit == 'COMMIT':
    
        try:
            device.commit_config()

    
        except Exception as inst:
            print '\nAn error occurred with the commit: '
            print type(inst)
            sys.exit(inst)
            print
    
        else:
            print 'Config committed'
    
    else:
        sys.exit('Script aborted by user')
    
else:
    print('No changes needed' u"\U0001F37A")
    device.discard_config()

device.close()