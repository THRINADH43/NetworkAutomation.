# Using Nx-OS and Python

from netmiko import ConnectHandler

device = ConnectHandler(device_type="cisco_nxos", ip="10.10.20.176", username="cisco", password="cisco")
command1 = device.send_command("show run")
command2 = device.send_command("show arp")
command3 = device.send_command("show ip int brief")
config = ["interface loopback0", "ipaddress 10.10.20.0 255.0.0.0"]
device.send_config_set(config)
command4 = device.send_command("show ip int brief")
command5 = device.send_command("ping 172.16.252.5")
print(f"Output of Command1: \n{command1}")
print(f"Output of Command2: \n{command2}")
print(f"Before setting the loopback ip : \n{command3}")
print(f"After setting the loopback ip : \n{command4}")
print(f"Ping result : \n{command5}")
device.disconnect()
