import os
import json
import pyudev
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv('usb_devices.env')

# Extrair a string JSON
devices_json = os.getenv('USB_DEVICES')

# Converter a string JSON de volta para um array
device_list = json.loads(devices_json)

# Lista de IDs de dispositivos autorizados (exemplo: [('VendorID', 'ProductID'), ...])
# Substitua com os IDs dos seus dispositivos autorizados
# authorized_devices = [ ('1d6b', '0002'), ('8087', '0026'), ('9636', '9311'), ('046d', 'c34b'), ('0bda', '5532'), ('1d6b', '0003')]
authorized_devices = device_list

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

# Função para verificar se o dispositivo é autorizado
def is_device_authorized(device):
    vendor_id = device.get('ID_VENDOR_ID')
    product_id = device.get('ID_MODEL_ID')
    return (vendor_id, product_id) in authorized_devices

# Função para desabilitar o dispositivo
def disable_device(device):
    device_sys_path = device.sys_path
    authorized_file = os.path.join(device_sys_path, 'authorized')
    try:
        with open(authorized_file, 'w') as f:
            f.write('0')
        print(f"Dispositivo desabilitado: {device.sys_name}")
    except IOError as e:
        print(f"Erro ao desabilitar dispositivo: {e}")

# Função para manipular eventos de dispositivo
def handle_event(device):
    if device.action == 'add':
        print(f"Dispositivo conectado: {device}")
        if not is_device_authorized(device):
            print(f"Dispositivo não autorizado: {device.sys_name}")
            disable_device(device)
    elif device.action == 'remove':
        print(f"Dispositivo desconectado: {device}")

# Monitorar eventos do dispositivo
for device in iter(monitor.poll, None):
    handle_event(device)
