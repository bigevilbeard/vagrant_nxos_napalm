# vagrant_nxos_napalm
Using Napalm on Vagrant and Nexus

# Set Up

- Download virtulal box
- Download 9000v switch https://software.cisco.com/download/home/286312239/type/282088129/release/7.0%25283%2529I7%25283%2529?i=!pp
- Intall Napalm pip install napalm

# Bring up Vagrant

- vagrant init nxos/7.0.3.I7.3
- vagrant up

# Set Up Nexus switch
- vagrant ssh

Enable:
```
 Nexus9000v# conf t
Enter configuration commands, one per line. End with CNTL/Z.
Nexus9000v(config)# feature scp-server
Nexus9000v(config)# feature nxapi
Nexus9000v(config)# end
Nexus9000v(config)# exit
```

Run python scripts - Enjoy.

