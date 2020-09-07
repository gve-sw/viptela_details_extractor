from csv import DictWriter
from configparser import ConfigParser
from cisco_sdwan.base.rest_api import Rest

devices=ConfigParser()
# Load configurations from devices.conf
devices.read('device.conf')

# Getting SDWAN section from the configuration file
device_sdwan=devices['sdwan']

output_filename='device_interfaces.csv'
# List of properties required for the devices properties
# https://sdwan-docs.cisco.com/Product_Documentation/Command_Reference/Command_Reference/vManage_REST_APIs/Device_Inventory_APIs/Connected_Devices

#device_attributes=['deviceId','system-ip','host-name','reachability','device-type','device-model','device-groups','connectedVManages','validity','state','local-system-ip']
device_attributes=['host-name','deviceId','reachability','status','state','device-type','device-groups','uuid','validity']
interface_attributes=['ifname','if-admin-status','af-type','ip-address']

export_fields= device_attributes + interface_attributes

# Get Devices from Inventory
sdwan_instance=Rest('https://{}'.format(device_sdwan["hostname"]),device_sdwan["username"], device_sdwan["password"])
device_data = sdwan_instance.get('device')['data']
sorted(device_data,key=lambda i: i.get('deviceId'))
device_interface_data = []

with open(output_filename, 'w', newline='') as csvfile:
    writer = DictWriter(csvfile, fieldnames=export_fields)
    # Write Header for the CSV file
    writer.writeheader()

    for device in device_data:
        try:
            current_device = dict(filter(lambda x: (x[0] in device_attributes), device.items()))
            # current_device_group_list=filter(lambda x: str(x).strip('"'),current_device['device-groups'])
            # current_device['device-groups']=';'.join(current_device_group_list)
            interfaces = sdwan_instance.get("device/interface?deviceId={}".format(device['deviceId']))['data']
            # sorted(interfaces, key=lambda i: (i['ifname'],i['af-type']))

            try:
                for interface in interfaces:
                    current_interface = dict(filter((lambda x: x[0] in interface_attributes), interface.items()))
                    device_interface_detail={}
                    device_interface_detail.update(current_device)
                    device_interface_detail.update(current_interface)
                    writer.writerow(device_interface_detail)
            except Exception as err:
                print(err)
                pass
        except Exception as err:
            writer.writerow(current_device)
            print(err)
            pass

print('The details have been exported as {}'.format(output_filename))