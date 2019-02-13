#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

#// R4-R3 reduce cost
#//R4-R2  increase cost

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
#// R4-R3 reduce cost - increase preference
	
for device in (ios_r1,ios_r3):
	net_connect = Netmiko(**device)
	print(net_connect.find_prompt())
	config_commands=['int fa1/0','ip ospf cost 1','do show run int fa1/0']
	#config_commands=['do sh ip int br']
	output=net_connect.send_config_set(config_commands)
	print(output)	

for device in (ios_r4,ios_r3):
	net_connect = Netmiko(**device)
	print(net_connect.find_prompt())
	config_commands=['int fa0/0','ip ospf cost 1','do show run int fa1/0']
	#config_commands=['do sh ip int br']
	output=net_connect.send_config_set(config_commands)
	print(output)	
	
#//R2-R1  increase cost - reduce preference

for device in (ios_r2,ios_r1):
    net_connect = Netmiko(**device)
    print(net_connect.find_prompt())
	config_commands=['int fa0/0','ip ospf cost 100','do sh run int fa0/0']
	#config_commands=['do sh ip int br']
    output=net_connect.send_config_set(config_commands)
	print(output)
	
for device in (ios_r2,ios_r4):
    net_connect = Netmiko(**device)
    print(net_connect.find_prompt())
	config_commands=['int fa1/0','ip ospf cost 100','do show run int fa1/0']
	#config_commands=['do sh ip int br']
    output=net_connect.send_config_set(config_commands)
	print(output)

	