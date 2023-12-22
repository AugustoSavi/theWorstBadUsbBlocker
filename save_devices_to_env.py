import pyudev
import json

context = pyudev.Context()
device_list = []

# Coletando informações dos dispositivos USB
for device in context.list_devices(subsystem='usb', DEVTYPE='usb_device'):
    vendor_id = device.get('ID_VENDOR_ID')
    product_id = device.get('ID_MODEL_ID')
    if vendor_id and product_id:
        device_list.append((vendor_id, product_id))

# Convertendo o array em uma string JSON
device_list_str = json.dumps(device_list)

# Salvando os dados em um arquivo .env
with open('usb_devices.env', 'w') as file:
    file.write(f"USB_DEVICES={device_list_str}\n")

print("Arquivo usb_devices.env criado com sucesso.")
