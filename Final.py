# final-drain

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
		
def undrain(ios_r1,ios_r2,ios_r3,ios_r4):
	for device in (ios_r1,ios_r2,ios_r3,ios_r4):
		net_connect = Netmiko(**device)
		print(net_connect.find_prompt())
		config_commands=['int fa0/0','ip ospf cost 1','int fa1/0','ip ospf cost 1']
		output=net_connect.send_config_set(config_commands)
	
###
		

def ur2(ios_r1,ios_r2,ios_r3,ios_r4):
#//R1-R3-R4-R3  increase cost - reduce preference
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

def ur3(ios_r1,ios_r2,ios_r3,ios_r4):
#//R1-R3-R4-R3  increase cost - reduce preference
	for device in (ios_r1,ios_r3):
		net_connect = Netmiko(**device)
		print(net_connect.find_prompt())
		config_commands=['int fa1/0','ip ospf cost 100','do show run int fa1/0']
		#config_commands=['do sh ip int br']
		output=net_connect.send_config_set(config_commands)
		print(output)	

	for device in (ios_r4,ios_r3):
		net_connect = Netmiko(**device)
		print(net_connect.find_prompt())
		config_commands=['int fa0/0','ip ospf cost 100','do show run int fa1/0']
		#config_commands=['do sh ip int br']
		output=net_connect.send_config_set(config_commands)
		print(output)	

#//R1-R2-R4 reduce cost - more preference

	for device in (ios_r2,ios_r1):
		net_connect = Netmiko(**device)
		print(net_connect.find_prompt())
		config_commands=['int fa0/0','ip ospf cost 1','do sh run int fa0/0']
		#config_commands=['do sh ip int br']
		output=net_connect.send_config_set(config_commands)
		print(output)
		
	for device in (ios_r2,ios_r4):
		net_connect = Netmiko(**device)
		print(net_connect.find_prompt())
		config_commands=['int fa1/0','ip ospf cost 1','do show run int fa1/0']
		#config_commands=['do sh ip int br']
		output=net_connect.send_config_set(config_commands)
		print(output)	


def choice(ios_r1,ios_r2,ios_r3,ios_r4):
	opt=0
	while(opt<=4):
		opt = int(input("Enter option \n 1 - Undrain \n 2 - Drain R2 \n 3 - Drain R3 \n 4 - Exit "))
		if(opt) == 1:
			undrain(ios_r1,ios_r2,ios_r3,ios_r4)
		if (opt) == 2:
			ur2(ios_r1,ios_r2,ios_r3,ios_r4)
		if(opt) == 3:
			ur3(ios_r1,ios_r2,ios_r3,ios_r4)
		if(opt)== 4:	
			sys.exit()
			
if __name__=="__main__":
		choice(ios_r1,ios_r2,ios_r3,ios_r4)
	
	