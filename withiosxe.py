# Using IOS-XE and Python
from netmiko import ConnectHandler

device = ConnectHandler(device_type="cisco_xe", ip="10.10.20.176", username="cisco", password="cisco")
command1 = device.send_command("show run")
command2 = device.send_command("show arp")
command3 = device.send_command("show ip int brief")
config = ["interface loopback0", "ip address 10.10.20.0 255.0.0.0"]
device.send_config_set(config)
command4 = device.send_command("show ip int brief")
command5 = device.send_command("ping 172.16.252.5")
print(f"Output of Command1: \n{command1}")
print(f"Output of Command2: \n{command2}")
print(f"Before setting loopback ip : \n{command3}")
print(f"After Setting loopback ip : \n{command4}")
print(f"Pinging 172.16.252.5 : \n{command5}")
device.disconnect()
