#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass



ios_r1= {
        'device_type':'cisco_ios',
        'username':'lab',
        'password':'lab123',
        'ip':'198.51.100.21',
        }
		
ios_r2={
        'device_type':'cisco_ios',
        'username':'lab',
        'password':'lab123',
        'ip':'198.51.100.22',
        }
ios_r3={
        'device_type':'cisco_ios',
        'username':'lab',
        'password':'lab123',
        'ip':'198.51.100.23',
        }		
ios_r4={
        'device_type':'cisco_ios',
        'username':'lab',
        'password':'lab123',
        'ip':'198.51.100.24'
        }
		
for device in (ios_r1,ios_r2,ios_r3,ios_r4):
    net_connect = Netmiko(**device)
    print(net_connect.find_prompt())
	config_commands=['int fa0/0','ip ospf cost 1','int fa1/0','ip ospf cost 1']
    output=net_connect.send_config_set(config_commands)